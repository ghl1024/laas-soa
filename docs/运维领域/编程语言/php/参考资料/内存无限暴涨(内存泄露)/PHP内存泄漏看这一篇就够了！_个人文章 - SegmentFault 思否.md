# [PHP内存泄漏看这一篇就够了！](https://segmentfault.com/a/1190000024464967)

[php](https://segmentfault.com/t/php)[swoole](https://segmentfault.com/t/swoole)

发布于 9月15日

![img](PHP内存泄漏看这一篇就够了！_个人文章 - SegmentFault 思否.assets/lg.php)

### FPM 的黑魔法

首先，传统的跑在 FPM 下的 PHP 代码是没有`“内存泄漏”`一说的，所谓的内存泄漏就是忘记释放内存，导致进程占用的`物理内存(附1)`**持续**增长，得益于 PHP 的短生命周期，PHP 内核有一个关键函数叫做`php_request_shutdown`此函数会在请求结束后，把请求期间申请的所有内存都释放掉，这从根本上杜绝了内存泄漏，极大的提高了 PHPer 的开发效率，同时也会导致性能的下降，例如单例对象，没必要每次请求都重新申请释放这个单例对象的内存。（这也是`Swoole`等`cli`方案的优势之一，因为 cli 请求结束不会清理内存）。

### Cli 下的内存泄漏

相信 PHPer 都遇见过这个报错`Fatal error: Allowed memory size of 134217728 bytes exhausted (tried to allocate 12288 bytes)`，是由于向 PHP 申请的内存达到了上限导致的，在 FPM 下一定是因为这次 web 请求有大内存块申请，例如 Sql 查询返回一个超大结果集，但在 Cli 下报这个错大概率是因为你的 PHP 代码出现了内存泄漏。

常见的泄漏姿势有：

- 向类的静态属性中追加数据，例如：

```
//不停的调用foo() 内存就会一直涨
function foo(){
        ClassA::$pro[] = "the big string";
}
```

- 向 &dollar;GLOBAL 全局变量中追加数据，例如：

```
//不停的调用foo() 内存就会一直涨
function foo(){
        $GLOBAL['arr'][] = "the big string";
}
```

- 向函数的静态变量中追加数据，例如：

```
//不停的调用foo() 内存就会一直涨
function foo(){
        static $arr = [];
        $arr[] = "the big string";
}
```

### 我们需要检测工具

有的同学可能会说很简单嘛，把追加的变量在请求结束后`unset()`掉就可以了。但真实场景远没有你想的那么简单：

- 例一：

```
function foo()
{
    $obj = new ClassA(); //foo函数结束后将自动释放 $obj对象
    $obj->pro[] = str_repeat("big string", 1024);
}

while (1) {
    foo();
    sleep(1);
}
```

> 上述代码 Cli 运行起来会泄漏吗？肉眼来看肯定不会泄漏，因为`foo()`函数结束后`$obj`是栈上的对象自动释放掉了，但答案是可能泄漏也可能没泄漏，这取决于`ClassA`的定义：

```
class classA
{
    public $pro;
    public function __construct()
    {
        $this->pro = &$GLOBALS['arr']; //pro是其他变量的引用
    }
}
```

> 如果`ClassA`的定义是上面的样子，那么这个例子就是泄漏的！！

- 例二：

```
class Test
{
    public $pro = null;
    function run()
    {
        $var = "Im global var now";//此处 $var 是长生命周期。
        $http = new \Swoole\Http\Server("0.0.0.0", 9501, SWOOLE_BASE);
        $http->on("request", function($req, $resp) {
            //此处没有给类的静态属性赋值，没有给全局变量赋值，
            //也没有给函数的静态变量赋值，但是这里是泄漏的，因为 $this 变成长生命周期了。
            $this->pro[] = str_repeat("big string", 1024);
            $resp->end("hello world");
        });
        $http->start();
        echo "run done\n"; //输出不了
        //这个函数永远不会结束，局部变量也变成了"全局变量"
    }

}
(new Test())->run();
```

> `new Test()`的本意虽然是创建一个临时的对象，但是`run()`方法触发了`server->start()`方法，代码将不向下执行，`run()`函数结束不了，`run()`函数的局部变量`$var`和临时对象本身都可以视为全局变量了，给其追加数据都是泄漏的！！

- 例三：

> 由于
>
> ```
> php_request_shutdown
> ```
>
> 的存在，很多 PHP 扩展其实是有内存泄漏的(emalloc 后没有 efree)，但是在 FPM 下是可以正常运行的，而这些扩展放到 Cli 下就会有内存泄漏问题，如果没有工具，Cli 下遇到扩展的泄漏问题，那也只能 gg 了-.-！
>
> 还有就是当我们调用第三方的类库的函数，要传一个参数，这个参数是全局变量，我不知道这个第三方库会不会给这个参数追加数据，一旦追加数据就会产生泄漏，同理别人给我的函数传的参数我也不敢赋值，第三方函数的返回值有没有全局变量我也不知道。

综上我们需要一个检测工具，相对于其他语言 PHP 在这个领域是空白的，可以说没有这个工具整个 Cli 生态就无法真正的发展起来，因为复杂的项目都会遇到泄漏问题。

[Swoole Tracker](https://business.swoole.com/tracker/index)可以检测泄漏问题，但它是一款商业产品，现在我们决定重构这个工具，把内存泄漏检测的功能（下文简称`Leak工具`）完全免费给 PHP 社区使用，完善 PHP 生态，回馈社区，下面我将概述它的具体用法和工作原理。

### Swoole Tracker 用法

`Leak工具`的实现原理是直接拦截系统底层的 emalloc，erealloc，以及 efree 调用，记录一个巨大的指针表，emalloc/erealloc 的时候添加，efree 的时候删除表中的记录，如果请求结束，指针表中仍然有值就证明产生了内存泄漏，不仅能发现 PHP 代码的泄漏，扩展层甚至 PHP 语言层面的泄漏都能发现，从根本上杜绝泄漏问题。

使用方式很简单：

- 前往官网[下载最新的 tracker(3.0+) 扩展](https://business.swoole.com/SwooleTracker/download/)。
- php.ini 加入以下配置：

```
extension=swoole_tracker.so
;总开关
apm.enable=1
;Leak检测开关
apm.enable_malloc_hook=1
```

- 在 Cli 模式下主业务逻辑一定是可以抽象成循环体函数的，例如`Swoole`的[OnReceive](https://wiki.swoole.com/#/server/events?id=onreceive)函数，workerman 的[OnMessage](http://doc3.workerman.net/315159)函数，以及上文例一中的`foo()`函数， 在循环体主函数(下文简称`主函数`)最开始加上`trackerHookMalloc()`调用即可：

```
function foo()
{
    trackerHookMalloc(); //标记主函数，开始hook malloc
    $obj = new ClassA();
    $obj->pro[] = str_repeat("big string", 1024);
}

while (1) {
    foo();
    sleep(1);
}
```

每次调用`主函数`结束后（第一次调用不会被记录），都会生成一个泄漏的信息到`/tmp/trackerleak`日志里面。

### 查看泄漏结果

在 Cli 命令行调用`trackerAnalyzeLeak()`函数即可分析泄漏日志，生成泄漏报告，可以直接`php -r "trackerAnalyzeLeak();"`即可。

下面是泄漏报告的格式：

- 没有内存泄漏的情况：

[16916 (Loop 5)] ✅ Nice!! No Leak Were Detected In This Loop

> 其中`16916`表示进程 id，`Loop 5`表示第 5 次调用`主函数`生成的泄漏信息

- 有确定的内存泄漏：

[24265 (Loop 8)] /Users/guoxinhua/tests/mem_leak/http_server.php:125 => <span style="color:red">[12928]</span>
[24265 (Loop 8)] /Users/guoxinhua/tests/mem_leak/http_server.php:129 => <span style="color:red">[12928]</span>
[24265 (Loop 8)] ❌ This Loop TotalLeak: <span style="color:red">[25216]</span>

> 表示第 8 次调用`http_server.php`的 125 行和 129 行，分别泄漏了 12928 字节内存，总共泄漏了 25216 字节内存。

通过调用`trackerCleanLeak()`可以清除泄漏日志，重新开始。

### 技术特性（技术难点）

- 支持持续增长检测：

想象一个场景，第一次请求运行`主函数`的时候申请 10 字节内存，然后请求结束前释放掉，然后第二次请求申请了 100 字节，请求结束再释放掉，虽然每次都能正确的释放内存但是每次又都申请更多的内存，最终导致内存爆掉，`Leak工具`支持这种检测，如果某一行代码有`N次`(默认 5 次)这种行为就会报`"可疑的内存泄漏"`，格式如下：

<span style="color:#b0b05f">The Possible Leak As Malloc Size Keep Growth:</span>
/Users/guoxinhua/tests/mem_leak/hook_malloc_incri.php:39 => <span style="color:red"> Growth Times : [8]; Growth Size : [2304]</span>

表示 39 行有 8 次 malloc size 的增长，总共增长了 2304 字节。

- 支持跨 loop 分析：

```
//Swoole Http Server的OnRequest回调
$http->on("request", function($request, $response) {
    trackerHookMalloc();

    if(isset(classA::$leak['tmp'])){
        unset(classA::$leak['tmp']);//每一次loop都释放上一次loop申请的内存
        }

    classA::$leak['tmp'] = str_repeat("big string", 1024);//申请内存 并在本次loop结束后不释放
    $response->end("hello world");
});
```

按照正常的检测泄漏的理论，上述代码每次都会检测出泄漏，因为每次都给`classA::$leak['tmp']`赋值并在 Loop 结束也没有释放，但实际业务代码经常这样写，并且此代码也是不会产生泄漏的，因为本次 Loop 的泄漏会在下次释放掉，`Leak工具`会**跨相邻 2 个**Loop 进行分析，自动对冲上面这种情况的泄漏信息，如果是跨多个 Loop 的释放，会以如下格式输出：

[28316 (Loop 2)] /Users/guoxinhua/tests/mem_leak/hook_efree_pre_loop.php:37 => <span style="color:red">[-12288]</span>
<span style="color:#5f92b0">Free Pre (Loop 0) : /Users/guoxinhua/tests/mem_leak/hook_efree_pre_loop.php:42 => [12288]</span>
[28316 (Loop 2)] /Users/guoxinhua/tests/mem_leak/hook_efree_pre_loop.php:42 => <span style="color:red">[12288]</span>
[28316 (Loop 2)] ✅ Nice!! No Leak Were Detected In This Loop

上述信息表示 Loop 2 释放了 Loop 0 的 12288 字节内存，然后 Loop 2 又申请了 12288 字节内存，总体来说本次 Loop 跑下来没有内存泄漏。

- 支持循环引用情况：

首先简单的介绍一下循环引用问题：

```
function foo()
{
    $o = new classA();
    $o->pro[] = $o;
    //foo结束后 $o无法释放，因为自己引用了自己，即循环引用
}

while (1) {
    foo();
    sleep(1);
}
```

因为循环引用，上面的代码每次运行`foo()`内存都会增长，但是这个代码确实没有内存泄漏的，因为增长到一定程度 PHP 会开启同步垃圾回收，把这种循环引用的内存都释放掉。

但是这给`Leak工具`带来了麻烦，因为`$o`的变量是延迟释放的，`foo()`结束后会报泄漏，而这种写法又确实不是泄漏。

`Swoole Tracker`的`Leak工具`会自动识别上面的情况，**会马上释放循环引用的内存**，不会造成误报。

> 如果你发现你的进程内存一直涨，开启了 Tracker 的泄漏检测，通过`memory_get_usage(false);`打印发现内存不涨了，那么证明你的应用存在循环引用，并且本来就没有内存泄漏问题。

- 支持子协程统计：

```
function loop()
{
      trackerHookMalloc();
      classA::$leak[] = str_repeat("big string", 1024);//申请内存
    go(function() {
        echo co::getcid() . "child\n";
        go(function() {
          echo co::getcid()."child2\n";
          classA::$leak = [];//释放内存
        });
    });
}

Co\run(function(){
    while (1) {
        loop();
        sleep(1);
    }
});
```

上述代码申请的内存会在第二个子协程里面释放，`Leak工具`会自动识别协程环境，会在所有子协程都结束后才统计汇总，所以上述代码不会有误报情况。

- 支持 defer，context：

```
$http->on("request", function($request, $response) {
    trackerHookMalloc();

    $context = Co::getContext();
    $context['data'] = str_repeat("big string", 1024);//context会在协程结束自动释放
    classA::$leak[] = str_repeat("big string1", 1024);
    defer(function() {
        classA::$leak = [];//注册defer释放内存
    });
    $response->end("hello world");
});
```

`Leak工具`会自动识别协程环境，如果存在 defer 和 context，会在 defer 执行结束和 context 释放之后再统计汇总，所以上述代码不会有误报情况，当然如果上面没有注册 defer 也会正确的报告泄漏信息。

- 支持旁路函数干扰排除：

例如一个进程由`主函数`响应请求（OnRequest 等），然后还有个定时器在运行（旁路函数），我们希望检测的是主循环函数的泄漏情况，而当主循环函数执行到一半的时候定时器函数执行了,并申请了内存，然后又切回到主循环函数，此时会误报，`Leak工具`会支持识别出旁路函数然后不收集旁路函数的 malloc 数据。

除了上述这些，`Leak工具`还支持`internd string`抓取等等，在此不再展开。

### 注意

- 前几次 Loop 的泄漏信息不用管，因为大部分项目都有一些初始化的缓存是不释放的。
- 检测期间尽量不要有并发。
- 由于开启泄漏检测后性能会非常差，不要在 php.ini 中开启`apm.enable_malloc_hook = 1`压测。
- 和 Swoole Tracker2.x 的检查泄漏原理不一样，不能一起用。
- 一个进程只能有一个地方调用`trackerHookMalloc()`函数。
- `Swoole4.5.3`由于底层 api 有问题，`Leak工具`无法正常工作，请升级到最新版`Swoole`或者降级`Swoole`版本。