\> 静态程序分析是对未实际执行程序的情况下执行的计算机软件的分析， [Wikipedia](https://en.wikipedia.org/wiki/Static_program_analysis)

这是静态分析工具和代码质量检查器的集合. 拉请求非常欢迎！

*：版权：代表专有软件. 所有其他工具都是开源的.* ：警告：表示社区不建议将此工具用于 已经过时或不再维护的新项目.

还要检查姐妹项目， [awesome-dynamic-analysis](https://github.com/mre/awesome-dynamic-analysis).

<details style="box-sizing: inherit; box-shadow: rgba(0, 0, 0, 0.14) 0px 2px 2px 0px, rgba(0, 0, 0, 0.12) 0px 1px 5px 0px, rgba(0, 0, 0, 0.2) 0px 3px 1px -2px; position: relative; margin: 1.5625em 0px; padding: 0px 0.6rem; border-left: 0.2rem solid rgb(68, 138, 255); border-radius: 0.1rem; font-size: 0.64rem; overflow: auto; display: block; color: rgba(0, 0, 0, 0.87); font-family: &quot;Fira Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="box-sizing: inherit; display: block; outline: none; cursor: pointer; margin: 0px -0.6rem; padding: 0.4rem 2rem; border-bottom: none; background-color: rgba(68, 138, 255, 0.1); font-weight: 700;">显示语言</summary></details>

------

## Programming Languages[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#programming-languages)

## ABAP[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#abap)

- [abaplint](https://github.com/larshp/abaplint) - 用 TypeScript 编写的 ABAP 的 Linter.
- [abapOpenChecks](https://github.com/larshp/abapOpenChecks) - 通过新的和可自定义的检查功能增强了 SAP Code Inspector.

## Ada[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#ada)

- [Codepeer](http://www.adacore.com/codepeer) - 检测运行时和逻辑错误
- [Polyspace for Ada](https://www.mathworks.com/products/polyspace-ada.html) ：copyright：- 提供代码验证，以证明源代码中不存在溢出，零除，越界数组访问以及某些其他运行时错误.
- [SPARK](http://www.spark-2014.org/about) ：copyright：-Ada 的静态分析和形式验证工具集
- [Understand](https://scitools.com/ada-programming-essential/) ：copyright：-IDE 为 Ada 和 VHDL 提供代码分析，标准测试，指标，图形，依赖性分析等.

## Awk[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#awk)

- [gawk --lint](https://www.gnu.org/software/gawk/manual/html_node/Options.html) - 警告关于可疑或不可移植到其他 awk 实现的构造.

## C[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#c)

- [Astrée](https://www.absint.com/astree/index.htm) ：copyright：- 基于 C / C ++ 抽象解释的声音静态分析器，可检测内存，类型和并发缺陷以及 MISRA 违规.
- [CBMC](http://www.cprover.org/cbmc/) - 用于 C 程序，用户定义的断言，标准断言，若干覆盖率度量分析的有界模型检查器
- [clang-tidy](http://clang.llvm.org/extra/clang-tidy/) -lang 静态分析
- [CMetrics](https://github.com/MetricsGrimoire/CMetrics) - 测量 C 文件的大小和复杂性
- [Codecheker](https://github.com/Ericsson/codechecker) - 使用 Web GUI 对 C / C ++ 代码进行静态分析
- [CodeSonar from GrammaTech](https://www.grammatech.com/products/codesonar) ：copyright：- 高级，整个程序，深层路径，对 C 和 C ++ 的静态分析以及易于理解的说明以及代码和路径可视化.
- [Corrode](https://github.com/jameysharp/corrode) - 从 C 到 Rust 的半自动翻译. 通过显示 Rust 编译器警告和错误，可以揭示原始实现中的错误.
- [cppcheck](https://github.com/danmar/cppcheck) -C / C ++ 代码的静态分析
- [CppDepend](https://www.cppdepend.com/) ：warning：：copyright：- 测量，查询和可视化您的代码，避免意外的问题，技术负担和复杂性.
- [cpplint](https://github.com/google/styleguide/tree/gh-pages/cpplint) - 遵循 Google 风格指南的自动 C ++ 检查器
- [cqmetrics](https://github.com/dspinellis/cqmetrics) -C 代码的质量指标
- [CScout](https://www.spinellis.gr/cscout/) -C 和 C 预处理程序代码的复杂度和质量指标
- [flawfinder](http://www.dwheeler.com/flawfinder/) - 发现可能的安全漏洞
- [flint++](https://github.com/JossWhittle/FlintPlusPlus) -flint 的跨平台，零依赖端口，这是 Facebook 开发和使用的用于 C ++ 的 lint 程序.
- [Frama-C](http://frama-c.com/) - 完善的 C 代码静态分析器
- [Helix QAC](https://www.perforce.com/products/helix-qac) ：copyright：- 嵌入式软件的企业级静态分析. 支持 MISRA，CERT 和 AUTOSAR 编码标准.
- [IKOS](https://github.com/nasa-sw-vnv/ikos) - 基于 LLVM 的 C / C ++ 代码的声音静态分析器
- [include-gardener](https://github.com/feddischson/include_gardener) - a multi-language static analyzer for C/C++/Obj-C/Python/Ruby to create a graph (in dot or graphml format) which shows all `#include` relations of a given set of files.
- [LDRA](https://ldra.com/) ：copyright：- 一个工具套件，包括对各种标准的静态分析（TBVISION），包括 MISRA C＆C ++，JSF ++ AV，CWE，CERT C，CERT C ++ 和自定义规则.
- [oclint](http://oclint.org/) -C / C ++ 代码的静态分析
- [Phasar](https://github.com/secure-software-engineering/phasar) - 基于 LLVM 的静态分析框架，带有污点和类型状态分析.
- [Polyspace Bug Finder](https://www.mathworks.com/products/polyspace-bug-finder.html) ：copyright：- 识别 C 和 C ++ 嵌入式软件中的运行时错误，并发问题，安全漏洞和其他缺陷.
- [Polyspace Code Prover](https://www.mathworks.com/products/polyspace-code-prover.html) ：copyright：- 提供代码验证，以证明 C 和 C ++ 源代码中不存在溢出，零除，越界数组访问以及某些其他运行时错误.
- [scan-build](https://clang-analyzer.llvm.org/scan-build.html) - 在编译时使用 LLVM 分析 C / C ++ 代码
- [splint](https://github.com/ravenexp/splint) - 注释辅助的静态程序检查器
- [SVF](https://github.com/SVF-tools/SVF) - 静态工具，可对 C 和 C ++ 程序进行可伸缩且精确的过程间相关性分析.
- [vera++](https://bitbucket.org/verateam/vera/wiki/Introduction) -Vera ++ 是用于验证，分析和转换 C ++ 源代码的可编程工具.

## C[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#c_1)

- [.NET Analyzers](https://github.com/DotNetAnalyzers) - 使用. NET 编译器平台开发分析器（诊断和代码修复）的组织.
- [Code Analysis Rule Collection](https://carc.codeplex.com/) - 包含在 Microsoft .NET 编译器平台 “Roslyn” 上构建的一组诊断程序，代码修复程序和重构程序.
- [code-cracker](https://github.com/code-cracker/code-cracker) - An analyzer library for C# and VB that uses Roslyn to produce refactorings, code analysis, and other niceties.
- [CodeRush](https://www.devexpress.com/products/coderush/) ：copyright：- 使用 Visual Studio 2015 及更高版本中的 Roslyn 引擎的代码创建，调试，导航，重构，分析和可视化工具.
- [CSharpEssentials](https://github.com/DustinCampbell/CSharpEssentials) - C# Essentials is a collection of Roslyn diagnostic analyzers, code fixes and refactorings that make it easy to work with C# 6 language features.
- [Designite](http://www.designite-tools.com/) ：copyright：-Designite 支持各种体系结构，设计和实现气味的检测，各种代码质量指标的计算以及趋势分析.
- [Gendarme](http://www.mono-project.com/docs/tools+libraries/tools/gendarme/) -Gendarme 检查包含 ECMA CIL 格式（Mono 和. NET）代码的程序和库.
- [NDepend](http://www.ndepend.com/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Measure, query and visualize your code and avoid unexpected issues, technical debt and complexity.
- [Puma Scan](https://github.com/pumasecurity/puma-scan) - 开发团队在 Visual Studio 中编写代码时，Puma Scan 提供了针对常见漏洞（XSS，SQLi，CSRF，LDAPi，加密，反序列化等）的实时安全代码分析.
- [Refactoring Essentials](https://marketplace.visualstudio.com/items?itemName=SharpDevelopTeam.RefactoringEssentialsforVisualStudio) - The free Visual Studio 2015 extension for C# and VB.NET refactorings, including code best practice analyzers.
- [ReSharper](https://www.jetbrains.com/resharper/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Extends Visual Studio with on-the-fly code inspections for C#, VB.NET, ASP.NET, JavaScript, TypeScript and other technologies.
- [Roslyn Analyzers](https://github.com/dotnet/roslyn-analyzers) - 基于 Roslyn 的 FxCop 分析仪实施.
- [Roslyn Security Guard](https://dotnet-security-guard.github.io/) - 该项目侧重于识别潜在漏洞，例如 SQL 注入，跨站点脚本（XSS），CSRF，加密漏洞，硬编码密码等.
- [Roslynator](https://github.com/JosefPihrt/Roslynator/) - A collection of 190+ analyzers and 190+ refactorings for C#, powered by Roslyn.
- [Security Code Scan](https://security-code-scan.github.io/) - Security code analyzer for C# and VB.NET. Detects various security vulnerability patterns: SQLi, XSS, CSRF, XXE, Open Redirect, etc.
- [SonarLint for Visual Studio](https://vs.sonarlint.org/) -SonarLint 是 Visual Studio 2015 和 2017 的扩展，可为开发人员提供即时反馈，以反馈有关. NET 代码中注入的新错误和质量问题.
- [VSDiagnostics](https://github.com/Vannevelj/VSDiagnostics) - 基于 Roslyn 并与 VS 集成的静态分析器集合.
- [Wintellect.Analyzers](https://github.com/Wintellect/Wintellect.Analyzers) -.NET 编译器平台（“Roslyn”）诊断分析器和代码修复.

## C++[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#c_2)

- [Astrée](https://www.absint.com/astree/index.htm) ：copyright：- 基于 C / C ++ 抽象解释的声音静态分析器，可检测内存，类型和并发缺陷以及 MISRA 违规.
- [CBMC](http://www.cprover.org/cbmc/) - 用于 C 程序，用户定义的断言，标准断言，若干覆盖率度量分析的有界模型检查器
- [clang-tidy](http://clang.llvm.org/extra/clang-tidy/) -lang 静态分析
- [CMetrics](https://github.com/MetricsGrimoire/CMetrics) - 测量 C 文件的大小和复杂性
- [Codecheker](https://github.com/Ericsson/codechecker) - 使用 Web GUI 对 C / C ++ 代码进行静态分析
- [CodeSonar from GrammaTech](https://www.grammatech.com/products/codesonar) ：copyright：- 高级，整个程序，深层路径，对 C 和 C ++ 的静态分析以及易于理解的说明以及代码和路径可视化.
- [Corrode](https://github.com/jameysharp/corrode) - 从 C 到 Rust 的半自动翻译. 通过显示 Rust 编译器警告和错误，可以揭示原始实现中的错误.
- [cppcheck](https://github.com/danmar/cppcheck) -C / C ++ 代码的静态分析
- [CppDepend](https://www.cppdepend.com/) ：warning：：copyright：- 测量，查询和可视化您的代码，避免意外的问题，技术负担和复杂性.
- [cpplint](https://github.com/google/styleguide/tree/gh-pages/cpplint) - 遵循 Google 风格指南的自动 C ++ 检查器
- [cqmetrics](https://github.com/dspinellis/cqmetrics) -C 代码的质量指标
- [CScout](https://www.spinellis.gr/cscout/) -C 和 C 预处理程序代码的复杂度和质量指标
- [flawfinder](http://www.dwheeler.com/flawfinder/) - 发现可能的安全漏洞
- [flint++](https://github.com/JossWhittle/FlintPlusPlus) -flint 的跨平台，零依赖端口，这是 Facebook 开发和使用的用于 C ++ 的 lint 程序.
- [Frama-C](http://frama-c.com/) - 完善的 C 代码静态分析器
- [Helix QAC](https://www.perforce.com/products/helix-qac) ：copyright：- 嵌入式软件的企业级静态分析. 支持 MISRA，CERT 和 AUTOSAR 编码标准.
- [IKOS](https://github.com/nasa-sw-vnv/ikos) - 基于 LLVM 的 C / C ++ 代码的声音静态分析器
- [include-gardener](https://github.com/feddischson/include_gardener) - a multi-language static analyzer for C/C++/Obj-C/Python/Ruby to create a graph (in dot or graphml format) which shows all `#include` relations of a given set of files.
- [LDRA](https://ldra.com/) ：copyright：- 一个工具套件，包括对各种标准的静态分析（TBVISION），包括 MISRA C＆C ++，JSF ++ AV，CWE，CERT C，CERT C ++ 和自定义规则.
- [oclint](http://oclint.org/) -C / C ++ 代码的静态分析
- [Phasar](https://github.com/secure-software-engineering/phasar) - 基于 LLVM 的静态分析框架，带有污点和类型状态分析.
- [Polyspace Bug Finder](https://www.mathworks.com/products/polyspace-bug-finder.html) ：copyright：- 识别 C 和 C ++ 嵌入式软件中的运行时错误，并发问题，安全漏洞和其他缺陷.
- [Polyspace Code Prover](https://www.mathworks.com/products/polyspace-code-prover.html) ：copyright：- 提供代码验证，以证明 C 和 C ++ 源代码中不存在溢出，零除，越界数组访问以及某些其他运行时错误.
- [scan-build](https://clang-analyzer.llvm.org/scan-build.html) - 在编译时使用 LLVM 分析 C / C ++ 代码
- [splint](https://github.com/ravenexp/splint) - 注释辅助的静态程序检查器
- [SVF](https://github.com/SVF-tools/SVF) - 静态工具，可对 C 和 C ++ 程序进行可伸缩且精确的过程间相关性分析.
- [vera++](https://bitbucket.org/verateam/vera/wiki/Introduction) -Vera ++ 是用于验证，分析和转换 C ++ 源代码的可编程工具.

## Crystal[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#crystal)

- [ameba](https://github.com/veelenga/ameba) - 用于 Crystal 的静态代码分析工具
- [crystal](https://crystal-lang.org/) -Crystal 编译器具有内置的棉绒功能.

## Delphi[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#delphi)

- [Fix Insight](https://www.tmssoftware.com/site/fixinsight.asp) ：copyright：- 一个免费的 IDE 插件，用于静态代码分析. _Pro_版本包括出于自动化目的的命令行工具.
- [Pascal Analyzer](https://peganza.com/products_pal.html) ：copyright：- 具有大量报告的静态代码分析工具. 提供免费的_Lite_版本，报告数量有限.
- [Pascal Expert](https://peganza.com/products_pex.html) ：copyright：- 用于代码分析的 IDE 插件. 包括 Pascal Analyzer 报告功能的一部分，并且可用于 Delphi 2007 及更高版本.

## Dlang[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#dlang)

- [D-scanner](https://github.com/dlang-community/D-Scanner) -D-Scanner 是用于分析 D 源代码的工具

## Elixir[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#elixir)

- [credo](https://github.com/rrrene/credo) - 静态代码分析工具，专注于代码一致性和教学.
- [sobelow](https://github.com/nccgroup/sobelow) -Phoenix 框架的安全性静态分析

## Elm[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#elm)

- [elm-analyse](https://stil4m.github.io/elm-analyse/) - 一种工具，可让您分析 Elm 代码，识别缺陷并应用最佳实践.

## Erlang[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#erlang)

- [elvis](https://github.com/inaka/elvis) -Erlang Style Reviewer
- [Primitive Erlang Security Tool (PEST)](https://github.com/okeuday/pest) - 一种对 Erlang 源代码进行基本扫描并报告可能导致 Erlang 源代码不安全的函数调用的工具.

## F[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#f)

- [FSharpLint](https://github.com/fsprojects/FSharpLint) -F 的皮棉工具#

## Fortran[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#fortran)

- [i-Code CNES for Fortran](https://github.com/lequal/i-CodeCNES) - 用于 Fortran 77，Fortran 90 和 Shell 的开源静态代码分析工具.

## Go[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#go)

- [aligncheck](https://gitlab.com/opennota/check) - 查找效率低下的打包结构.
- [bodyclose](https://github.com/timakin/bodyclose) - 检查 HTTP 响应主体是否关闭.
- [deadcode](https://github.com/tsenart/deadcode) - 查找未使用的代码.
- [dingo-hunter](https://github.com/nickng/dingo-hunter) - 用于在 Go 中查找死锁的静态分析器.
- [dogsled](https://github.com/alexkohler/dogsled) - 查找带有太多空白标识符的分配 / 声明.
- [dupl](https://github.com/mibk/dupl) - 报告可能重复的代码.
- [errcheck](https://github.com/kisielk/errcheck) - 检查是否使用错误返回值.
- [flen](https://github.com/lafolle/flen) - 在 Go 软件包中获取有关函数长度的信息.
- [gas](https://github.com/GoASTScanner/gas) - 通过扫描 Go AST 检查源代码是否存在安全问题.
- [Go Meta Linter](https://github.com/alecthomas/gometalinter) ：warning：- 同时运行 Go lint 工具并标准化其输出. 将`golangci-lint`用于新项目.
- [go tool vet --shadow](https://golang.org/cmd/vet/#hdr-Shadowed_variables) - 报告可能被意外遮盖的变量.
- [go vet](https://golang.org/cmd/vet/) - 检查 Go 源代码并报告可疑.
- [go-consistent](https://github.com/Quasilyte/go-consistent) - 分析器，可帮助您使 Go 程序更加一致.
- [go-critic](https://github.com/go-critic/go-critic) - 保留检查当前未在其他 linter 中实现的检查的源代码 linter.
- [go/ast](https://golang.org/pkg/go/ast/) - 包 ast 声明用于表示 Go 包的语法树的类型.
- [gochecknoglobals](https://github.com/leighmcculloch/gochecknoglobals) - 检查是否没有全局变量.
- [goconst](https://github.com/jgautheron/goconst) - 查找可以被常量替换的重复字符串.
- [gocyclo](https://github.com/fzipp/gocyclo) - 计算 Go 源代码中函数的圈复杂度.
- [gofmt -s](https://golang.org/cmd/gofmt/) - 检查代码格式是否正确，是否无法进一步简化.
- [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) - 检查丢失或未引用的程序包导入.
- [GolangCI-Lint](https://github.com/golangci/golangci-lint) - 替代 “Go Meta Linter”：GolangCI-Lint 是一个 Linters 聚合器.
- [golint](https://github.com/golang/lint) - 在 Go 源代码中打印出编码样式错误.
- [goreporter](https://github.com/360EntSecGroup-Skylar/goreporter) - 同时运行许多 linter，并将其输出标准化为报告.
- [goroutine-inspect](https://github.com/linuxerwang/goroutine-inspect) - 分析 Golang goroutine 转储的交互式工具.
- [gosec (gas)](https://github.com/GoASTScanner/gas) - 通过扫描 Go AST 检查源代码是否存在安全问题.
- [gosimple](https://godoc.org/github.com/surullabs/lint/gosimple) - 简化代码.
- [gotype](https://golang.org/x/tools/cmd/gotype) - 类似于 Go 编译器的语法和语义分析.
- [ineffassign](https://github.com/gordonklaus/ineffassign) - 在 Go 代码中检测无效的分配
- [interfacer](https://github.com/mvdan/interfacer) - 建议使用较窄的接口.
- [lll](https://github.com/walle/lll) - 报告长行.
- [maligned](https://github.com/mdempsky/maligned) - 检测对字段进行排序会占用较少内存的结构.
- [misspell](https://github.com/client9/misspell) - 查找通常拼写错误的英语单词.
- [nakedret](https://github.com/alexkohler/nakedret) - 寻找赤裸裸的回报.
- [nargs](https://github.com/alexkohler/nargs) - 在函数声明中查找未使用的参数.
- [prealloc](https://github.com/alexkohler/prealloc) - 查找可能预先分配的切片声明.
- [revive](https://github.com/mgechev/revive) -Go 的快速，可配置，可扩展，灵活和美观的 Linter. 即插即用替换的小垫布.
- [safesql](https://github.com/stripe/safesql) - 用于 Golang 的静态分析工具，可防止 SQL 注入.
- [staticcheck](https://staticcheck.io/) - A suite of static analysis tools for Go, similar to ReSharper for C#. It specialises on bug finding, code simplicity, performance and editor integration.
- [structcheck](https://gitlab.com/opennota/check) - 查找未使用的结构字段.
- [test](http://golang.org/pkg/testing/) - 从 stdlib 测试模块显示测试失败的位置.
- [unconvert](https://github.com/mdempsky/unconvert) - 检测冗余类型转换.
- [unimport](https://github.com/alexkohler/unimport) - 查找不必要的导入别名
- [unparam](https://github.com/mvdan/unparam) - 查找未使用的功能参数.
- [unused](https://github.com/dominikh/go-tools/tree/master/unused) - 查找未使用的变量.
- [varcheck](https://gitlab.com/opennota/check) - 查找未使用的全局变量和常量.
- [wsl](https://github.com/bombsimon/wsl) - 在正确的地方插入空行.

## Groovy[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#groovy)

- [CodeNarc](https://github.com/CodeNarc/CodeNarc) - 用于 Groovy 源代码的静态分析工具，可以监视和执行许多编码标准和最佳实践

## Haskell[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#haskell)

- [HLint](https://github.com/ndmitchell/hlint) -HLint 是用于建议对 Haskell 代码进行可能的改进的工具.
- [Weeder](https://github.com/ndmitchell/weeder) - 使用 Haskell 代码检测无效出口或包裹进口的工具.

## Haxe[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#haxe)

- [Haxe Checkstyle](https://github.com/HaxeCheckstyle/haxe-checkstyle) - 静态分析工具，可帮助开发人员编写符合编码标准的 Haxe 代码.

## Java[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#java)

- [Checker Framework](https://github.com/typetools/checker-framework/) -Java 的可插拔类型检查 http://checkerframework.org/
- [checkstyle](https://github.com/checkstyle/checkstyle) - 检查 Java 源代码是否符合代码标准或一组验证规则（最佳做法）
- [ck](https://github.com/mauricioaniche/ck) - 通过处理源 Java 文件来计算 Chidamber 和 Kemerer 面向对象的指标
- [ckjm](http://www.spinellis.gr/sw/ckjm/) - 通过处理已编译的 Java 文件的字节码来计算 Chidamber 和 Kemerer 的面向对象的指标
- [CogniCrypt](https://www.eclipse.org/cognicrypt/) - 检查 Java 源代码和字节码是否正确使用了加密 API
- [DesigniteJava](http://www.designite-tools.com/designitejava) ：copyright：-DesigniteJava 支持各种体系结构，设计和实现气味的检测以及各种代码质量指标的计算.
- [Error-prone](https://github.com/google/error-prone) - 捕获常见的 Java 错误作为编译时错误
- [fb-contrib](https://github.com/mebigfatguy/fb-contrib) - 具有附加错误检测器的 FindBugs 插件
- [Find Security Bugs](https://find-sec-bugs.github.io/) -IDE / SonarQube 插件，用于 Java Web 应用程序的安全审核.
- [forbidden-apis](https://github.com/policeman-tools/forbidden-apis) - 检测并禁止调用特定的方法 / 类 / 字段（例如从没有字符集的文本流中读取）. Maven / Gradle / Ant 兼容.
- [google-java-format](https://github.com/google/google-java-format) -Google 样式重新格式化
- [Hopper](https://github.com/cuplv/hopper) - 用 scala 编写的针对 JVM 上运行的语言的静态分析工具
- [HuntBugs](https://github.com/amaembo/huntbugs) ：warning：- 基于 Procyon 编译器工具的字节码静态分析器工具，旨在取代 FindBugs.
- [JArchitect](https://www.jarchitect.com/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Measure, query and visualize your code and avoid unexpected issues, technical debt and complexity.
- [JBMC](http://www.cprover.org/jbmc/) -Java 的有限模型检查器（字节码），验证用户定义的断言，标准断言，若干覆盖率度量分析
- [NullAway](https://github.com/uber/NullAway) - 基于类型的空指针检查器，具有较低的构建时间开销； 一个 [Error Prone](http://errorprone.info/) 插入
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/) - 检查依赖项是否存在已知的，公开披露的漏洞.
- [qulice](https://www.qulice.com/) - 结合了一些（预配置）静态分析工具（checkstyle，PMD，Findbugs 等）.
- [Soot](https://sable.github.io/soot/) - 用于分析和转换 Java 和 Android 应用程序的框架.
- [Spoon](https://github.com/INRIA/spoon) - 为 Java 编写自己的静态分析和体系结构规则检查器的库. 可以集成在 Maven 和 Gradle 中.
- [SpotBugs](https://spotbugs.github.io/) -SpotBugs 是 FindBugs 的继任者. 静态分析工具，用于查找 Java 代码中的错误.
- [Xanitizer](https://xanitizer.com/) -Xanitizer 在 Java / Scala Web 应用程序中发现安全漏洞.

## JavaScript[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#javascript)

- [aether](https://github.com/codecombat/aether) - 在节点或浏览器中衬入，分析，规范化，转换，沙盒，运行，逐步浏览和可视化用户 JavaScript.
- [Closure Compiler](https://github.com/google/closure-compiler) - 一种编译器工具，可提高效率，减小大小并在 JavaScript 文件中提供代码警告.
- [ClosureLinter](https://github.com/google/closure-linter) ：warning：- 确保您所有项目的 JavaScript 代码均遵循 Google JavaScript 样式指南中的指南. 它还可以自动修复许多常见错误
- [coffeelint](https://github.com/clutchski/coffeelint) - 样式检查器，可帮助确保 CoffeeScript 代码保持干净和一致.
- [complexity-report](https://github.com/jared-stilwell/complexity-report) ：警告：-JavaScript 项目的软件复杂性分析
- [DeepScan](https://deepscan.io/) ：copyright：- 一个 JavaScript 分析器，它针对运行时错误和质量问题，而不是编码约定.
- [escomplex](https://github.com/jared-stilwell/escomplex) -JavaScript 系列抽象语法树的软件复杂性分析.
- [eslint](https://github.com/eslint/eslint) - 完全可插拔的工具，用于识别和报告 JavaScript 模式
- [Esprima](https://github.com/jquery/esprima) - 用于多用途分析的 ECMAScript 解析基础结构
- [flow](https://flow.org/) -JavaScript 的静态类型检查器.
- [hegel](https://jsmonk.github.io/hegel) -JavaScript 的静态类型检查器，带有类型推断偏向和强类型系统.
- [jshint](https://github.com/jshint/jshint) ：warning：- 检测 JavaScript 代码中的错误和潜在问题，并执行团队的编码约定
- [JSLint](https://github.com/douglascrockford/JSLint) ：警告：-JavaScript 代码质量工具
- [JSPrime](https://github.com/dpnishant/jsprime) - 静态安全分析工具
- [NodeJSScan](https://github.com/ajinabraham/NodeJsScan) -NodeJsScan 是用于 Node.js 应用程序的静态安全代码扫描程序.
- [plato](https://github.com/es-analysis/plato) - 可视化 JavaScript 源复杂度
- [Prettier](https://github.com/prettier/prettier) - 固执己见的代码格式化程序.
- [quality](https://github.com/jden/quality) - 零配置代码和模块棉绒
- [retire.js](https://github.com/RetireJS/retire.js) - 扫描程序检测已知漏洞的 JavaScript 库的使用
- [standard](http://standardjs.com/) - 一个 npm 模块，用于检查 Javascript Styleguide 问题
- [tern](https://github.com/ternjs/tern) -JavaScript 代码分析器，可提供深入的跨编辑器语言支持
- [xo](https://github.com/xojs/xo) - 固执己见，但可配置的 ESLint 包装器，其中包含许多好东西. 强制执行严格且易读的代码.
- [yardstick](https://github.com/calmh/yardstick) ：警告：-Javascript 代码指标

## Kotlin[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#kotlin)

- [detekt](https://github.com/arturbosch/detekt) -Kotlin 代码的静态代码分析.
- [ktlint](https://github.com/shyiko/ktlint) - 带有内置格式化程序的防骑自行车科特林短绒

## Lua[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#lua)

- [luacheck](https://github.com/mpeterv/luacheck) - 用于 Lua 代码的整理和静态分析的工具.

## MATLAB[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#matlab)

- [mlint](https://de.mathworks.com/help/matlab/ref/mlint.html) ：copyright：- 检查 MATLAB 代码文件是否存在问题.

## PHP[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#php)

- [dephpend](https://github.com/mihaeu/dephpend) - 依赖性分析工具
- [deprecation-detector](https://github.com/sensiolabs-de/deprecation-detector) - 查找不推荐使用的（Symfony）代码的用法
- [deptrac](https://github.com/sensiolabs-de/deptrac) - 实施有关软件层之间依赖性的规则.
- [DesignPatternDetector](https://github.com/Halleck45/DesignPatternDetector) - 检测 PHP 代码中的设计模式
- [EasyCodingSt 和 ard](https://github.com/Symplify/EasyCodingSt和ard) - 结合 [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) 和 [PHP-CS-Fixer](https://github.com/FriendsOfPHP/PHP-CS-Fixer)
- [exakat](https://github.com/exakat/exakat) - 用于 PHP 的自动代码审查引擎
- [GrumPHP](https://github.com/phpro/grumphp) - 每次提交时检查代码
- [Mondrian](https://github.com/Trismegiste/Mondrian) - 使用图论的一组静态分析和重构工具
- [parallel-lint](https://github.com/php-parallel-lint/PHP-Parallel-Lint) - 该工具检查 PHP 文件的语法的速度比带有高级输出的串行检查速度快.
- [Parse](https://github.com/psecio/parse) - 静态安全扫描仪
- [pdepend](https://pdepend.org/) - 计算软件度量，例如 PHP 代码的圈复杂度.
- [phan](https://github.com/etsy/phan) -etsy 的现代静电分析仪
- [PHP Architecture Tester](https://github.com/carlosas/phpat) - 易于使用的 PHP 体系结构测试工具.
- [PHP Assumptions](https://github.com/rskuipers/php-assumptions) - Checks for weak assumptions
- [PHP Coding Standards Fixer](http://cs.sensiolabs.org/) - 根据 PSR-1，PSR-2 和 Symfony 标准等标准修复代码.
- [Php Inspections (EA Extended)](https://github.com/kalessil/phpinspectionsea) - 用于 PHP 的静态代码分析器.
- [PHP Refactoring Browser](https://github.com/QafooLabs/php-refactoring-browser) - 重构助手
- [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) - 根据语义版本建议下一个版本
- [PHP-Parser](https://github.com/nikic/PHP-Parser) - 用 PHP 编写的 PHP 解析器
- [PHP-Token-Reflection](https://github.com/Andrewsville/PHP-Token-Reflection) - 库模拟 PHP 内部反射
- [php7cc](https://github.com/sstalle/php7cc) -PHP 7 兼容性检查器
- [php7mar](https://github.com/Alexia/php7mar) - 协助开发人员将其代码快速移植到 PHP 7
- [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) - 检测违反已定义的一组编码标准
- [phpca](https://github.com/wapmorgan/PhpCodeAnalyzer) - 查找非内置扩展名的用法
- [phpcf](http://wapmorgan.github.io/PhpCodeFixer/) - 查找不推荐使用的 PHP 功能的用法
- [phpcpd](https://github.com/sebastianbergmann/phpcpd) - 用于 PHP 代码的复制 / 粘贴检测器.
- [phpdcd](https://github.com/sebastianbergmann/phpdcd) -PHP 代码的死代码检测器（DCD）.
- [PhpDependencyAnalysis](https://github.com/mamuz/PhpDependencyAnalysis) - 为项目建立依赖图
- [phpdoc-to-typehint](https://github.com/dunglas/phpdoc-to-typehint) - 使用 PHPDoc 批注添加标量类型提示并向现有的 PHP 项目返回类型
- [phpDocumentor](https://www.phpdoc.org/) - 分析 PHP 源代码以生成文档
- [PHPMD](https://phpmd.org/) - 在代码中找到可能的错误
- [PhpMetrics](http://www.phpmetrics.org/) - 计算和可视化各种代码质量指标
- [phpmnd](https://github.com/povils/phpmnd) - 有助于检测魔术数字
- [PHPQA](https://github.com/EdgedesignCZ/phpqa) - 用于运行质量检查工具的工具（phploc，phpcpd，phpcs，pdepend，phpmd，phpmetrics）
- [phpqa - jakzal](https://github.com/jakzal/phpqa) - 在一个容器中有许多用于 PHP 静态分析的工具
- [phpqa - jmolivas](https://github.com/jmolivas/phpqa) -PHPQA 多合一分析器 CLI 工具
- [phpsa](https://github.com/ovr/phpsa) - 用于 PHP 的静态分析工具.
- [PHPStan](https://github.com/phpstan/phpstan) -PHP 静态分析工具 - 无需运行即可发现代码中的错误！
- [Progpilot](https://github.com/designsecurity/progpilot) - 出于安全目的的静态分析工具
- [Psalm](https://getpsalm.org/) - 用于在 PHP 应用程序中查找类型错误的静态分析工具
- [Qafoo Quality Analyzer](https://github.com/Qafoo/QualityAnalyzer) - 可视化指标和源代码
- [RIPS](https://www.ripstech.com/) ：copyright：- 静态源代码分析器，用于 PHP 脚本中的漏洞
- [Tuli](https://github.com/ircmaxell/Tuli) - 静态分析引擎
- [twig-lint](https://github.com/asm89/twig-lint) -twig-lint 是用于您的 twig 文件的皮棉工具.
- [WAP](https://securityonline.info/owasp-wap-web-application-protection-project/) - 用于检测和纠正 PHP（4.0 或更高版本）Web 应用程序中的输入验证漏洞的工具，并通过结合静态分析和数据挖掘来预测误报.

## Perl[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#perl)

- [Perl::Critic](https://metacpan.org/pod/Perl::Critic) -Critique Perl 最佳实践的源代码.

## Python[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#python)

- [bandit](https://github.com/PyCQA/bandit) - 在 Python 代码中查找常见安全问题的工具
- [bellybutton](https://github.com/hchasestevens/bellybutton) - 支持自定义项目特定规则的整理引擎
- [Black](https://github.com/ambv/black) - 毫不妥协的 Python 代码格式化程序
- [cohesion](https://github.com/mschwager/cohesion) - 用于测量 Python 类内聚力的工具
- [Dlint](https://github.com/dlint-py/dlint) - 确保 Python 代码安全的工具
- [include-gardener](https://github.com/feddischson/include_gardener) - a multi-language static analyzer for C/C++/Obj-C/Python/Ruby to create a graph (in dot or graphml format) which shows all `#include` relations of a given set of files.
- [jedi](https://github.com/davidhalter/jedi) - 适用于 Python 的自动完成 / 静态分析库
- [linty fresh](https://github.com/lyft/linty_fresh) - 解析皮棉错误并将其作为请求请求的注释报告给 Github
- [mccabe](https://github.com/PyCQA/mccabe) - 检查 McCabe 的复杂性
- [mypy](https://github.com/python/mypy) - 静态类型检查器，旨在结合经常使用的鸭子类型和静态类型的优点 [MonkeyType](https://github.com/Instagram/MonkeyType)
- [py-find-injection](https://github.com/uber/py-find-injection) - 在 Python 代码中查找 SQL 注入漏洞
- [pycodestyle](https://github.com/PyCQA/pycodestyle) -（以前是`pep8`）根据 PEP 8 中的某些样式约定检查 Python 代码
- [pydocstyle](https://github.com/PyCQA/pydocstyle) - 检查是否符合 Python 文档字符串约定
- [pyflakes](https://github.com/pyflakes/pyflakes/) - 检查 Python 源文件是否有错误
- [pylint](https://github.com/PyCQA/pylint) - 查找编程错误，帮助实施编码标准并嗅探某些代码气味. 它还包括 “pyreverse”（UML 图生成器）和 “ symilar”（相似性检查器）.
- [pyre-check](https://github.com/facebook/pyre-check) - 适用于大型 Python 代码库的快速，可扩展的类型检查器
- [pyright](https://github.com/Microsoft/pyright) - 用于 Python 的静态类型检查器，用于解决 mypy 等现有工具中的空白.
- [pyroma](https://github.com/regebro/pyroma) - 评估 Python 项目与 Python 打包生态系统的最佳实践的符合程度，并列出可以改进的问题
- [PyT - Python Taint](https://github.com/python-security/pyt) - 用于检测 Python Web 应用程序中的安全漏洞的静态分析工具.
- [pytype](https://github.com/google/pytype) - 用于 Python 代码的静态类型分析器.
- [radon](https://github.com/rubik/radon) - 一个 Python 工具，可从源代码计算各种指标
- [vulture](https://github.com/jendrikseipp/vulture) - 在 Python 代码中找到未使用的类，函数和变量
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide) - 有史以来最严格，最有主见的 python linter
- [wily](https://github.com/tonybaloney/wily) - 用于归档，探索和绘制 Python 源代码复杂性的命令行工具
- [xenon](https://github.com/rubik/xenon) - 使用以下命令监视代码复杂性 [`radon`](https://github.com/rubik/radon)

## Python wrappers[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#python-wrappers)

- [ciocheck](https://github.com/ContinuumIO/ciocheck) -lint，格式化程序和测试套件帮助器. 作为短绒棉，它是包裹在 “pep8”，“ pydocstyle”，“ flake8” 和“ pylint”周围的包装纸.
- [flake8](https://github.com/PyCQA/flake8) - 围绕 pyflakes，pycodestyle 和 mccabe 的包装器
- [multilint](https://github.com/adamchainz/multilint) - 围绕 “flake8”，“ isort” 和“ modernize”的包装器
- [prospector](https://github.com/PyCQA/prospector) - 在`pylint`，`pep8`，`mccabe`等周围包装

## R[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#r)

- [cyclocomp](https://github.com/MangoTheCat/cyclocomp) - 量化 R 函数 / 表达式的圈复杂度.
- [goodpractice](http://mangothecat.github.io/goodpractice/) - 分析 R 软件包的源代码并提供最佳实践建议.
- [lintr](https://github.com/jimhester/lintr) -R 的静态代码分析.
- [styler](https://styler.r-lib.org/) -R 源代码文件的格式和 R 代码的漂亮打印.

## RPG[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#rpg)

- [SourceMeter](https://www.sourcemeter.com/resources/rpg/) ：copyright：-RPG III 和 RPG IV 版本的静态代码分析（包括自由格式）

## Ruby[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#ruby)

- [brakeman](https://github.com/presidentbeef/brakeman) - 用于 Ruby on Rails 应用程序的静态分析安全漏洞扫描程序
- [cane](https://github.com/square/cane) - 代码质量阈值检查作为构建的一部分
- [dawnscanner](https://github.com/thesp0nge/dawnscanner) - 用于 ruby 编写的 Web 应用程序的静态分析安全扫描程序. 它支持 Sinatra，Padrino 和 Ruby on Rails 框架.
- [flay](https://github.com/seattlerb/flay) -Flay 分析代码的结构相似性.
- [flog](https://github.com/seattlerb/flog) -Flog 在易于阅读的疼痛报告中报告了遭受最多折磨的代码. 分数越高，代码所处的痛苦就越大.
- [include-gardener](https://github.com/feddischson/include_gardener) - a multi-language static analyzer for C/C++/Obj-C/Python/Ruby to create a graph (in dot or graphml format) which shows all `#include` relations of a given set of files.
- [laser](https://github.com/michaeledgar/laser) -Ruby 代码的静态分析和样式查询.
- [pelusa](https://github.com/codegram/pelusa) - 静态分析 Lint 型工具，可改善您的 OO Ruby 代码
- [quality](https://github.com/apiology/quality) - 使用社区工具对代码进行质量检查，并确保您的代码不会随着时间的推移而恶化.
- [Querly](https://github.com/soutaro/querly) - 基于模式的 Ruby 检查工具
- [Railroader](https://railroader.org/) - 针对 Ruby on Rails 应用程序的开源静态分析安全漏洞扫描程序.
- [reek](https://github.com/troessner/reek) -Ruby 代码气味检测器
- [RuboCop](https://github.com/rubocop-hq/rubocop) - 基于社区 Ruby 样式指南的 Ruby 静态代码分析器.
- [Rubrowser](https://github.com/blazeeboy/rubrowser) -Ruby 类交互式依赖图生成器.
- [ruby-lint](https://github.com/YorickPeterse/ruby-lint) -Ruby 的静态代码分析
- [rubycritic](https://github.com/whitesmith/rubycritic) -Ruby 代码质量报告程序
- [SandiMeter](https://github.com/makaroni4/sandi_meter) - 用于检查 Ruby 代码中 Sandi Metz 规则的静态分析工具.
- [Sorbet](https://github.com/sorbet/sorbet) - 专为 Ruby 设计的快速，强大的类型检查器

## Rust[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#rust)

- [cargo-audit](https://github.com/RustSec/cargo-audit) - 审核 Cargo.lock，以将带有安全漏洞的板条箱报告给 [RustSec Advisory Database](https://github.com/RustSec/advisory-db/).
- [cargo-inspect](https://github.com/mre/cargo-inspect) - 在没有语法糖的情况下检查 Rust 代码，以了解编译器的幕后工作.
- [clippy](https://github.com/Manishearth/rust-clippy) - 防止常见错误并改进 Rust 代码的代码仓库
- [electrolysis](https://github.com/Kha/electrolysis) - A tool for formally verifying Rust programs by transpiling them into definitions in the Lean theorem prover.
- [herbie](https://github.com/mcarton/rust-herbie-lint) - 在使用数值不稳定的浮点表达式时，在包装箱中添加警告或错误.
- [linter-rust](https://github.com/AtomLinter/linter-rust) - 使用 Rustc 和货物在 Atom 中整理您的 Rust 文件
- [MIRAI](https://github.com/facebookexperimental/MIRAI) - 使用 Rust 的中级中间语言操作的抽象解释器，并基于污点分析提供警告.
- [Rust Language Server](https://github.com/rust-lang-nursery/rls) - 支持诸如 “转到定义”，符号搜索，重新格式化和代码完成之类的功能，并支持重命名和重构.
- [rustfix](https://github.com/killercup/rustfix) - 阅读并应用 rustc（和第三方皮棉，如 clippy 所提供的皮棉）提出的建议.

## SQL[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#sql)

- [sqlcheck](https://github.com/jarulraj/sqlcheck-old) - 自动识别 SQL 查询中的反模式
- [sqlint](https://github.com/purcell/sqlint) - 简单的 SQL linter
- [tsqllint](https://github.com/tsqllint/tsqllint) -T-SQL 专用的 linter
- [TSqlRules](https://github.com/ashleyglee/TSqlRules) -SQL Server 的 TSQL 静态代码分析规则

## Scala[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#scala)

- [linter](https://github.com/HairyFotr/linter) -Linter 是一个 Scala 静态分析编译器插件，它为各种可能的 bug，效率低下和样式问题添加了编译时检查.
- [Scalastyle](http://www.scalastyle.org/) -Scalastyle 检查您的 Scala 代码并指出其潜在问题.
- [scapegoat](https://github.com/sksamuel/scapegoat) - 用于静态代码分析的 Scala 编译器插件
- [WartRemover](https://github.com/puffnfresh/wartremover) - 灵活的 Scala 代码整理工具.
- [Xanitizer](https://xanitizer.com/) -Xanitizer 在 Java / Scala Web 应用程序中发现安全漏洞.

## Shell[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#shell)

- [i-Code CNES for Shell](https://github.com/lequal/i-CodeCNES) - 用于 Shell 和 Fortran（77 和 90）的开源静态代码分析工具.
- [shellcheck](https://github.com/koalaman/shellcheck) -ShellCheck，一种静态分析工具，可为 bash / sh shell 脚本提供警告和建议

## Solidity[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#solidity)

- [slither](https://github.com/trailofbits/slither) - 静态分析框架，该框架运行一套漏洞检测器，打印有关合同明细的可视信息，并提供可轻松编写自定义分析的 API
- [solium](https://github.com/duaraghav8/Solium) -Solium 是一台可以识别和修复 Solidity 智能合约中的样式和安全问题的工具

## Swift[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#swift)

- [SwiftFormat](https://github.com/nicklockwood/SwiftFormat) - 用于重新格式化 Swift 代码的库和命令行格式化工具
- [SwiftLint](https://github.com/realm/SwiftLint) - 实施 Swift 样式和约定的工具
- [Tailor](https://github.com/sleekbyte/tailor) ：warning：- 用于以 Apple 的 Swift 编程语言编写的源代码的静态分析和棉绒工具.

## Tcl[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#tcl)

- [Frink](https://catless.ncl.ac.uk/Programs/Frink/) -Tcl 格式化和静态检查程序（可以美化该程序，将其最小化，混淆或仅对其进行完整性检查）.
- [Nagelfar](https://sourceforge.net/projects/nagelfar/) -Tcl 的静态语法检查器
- [tclchecker](https://github.com/ActiveState/tdk/blob/master/docs/3.0/TDK_3.0_Checker.txt) - 静态语法分析模块（作为 [TDK](https://github.com/ActiveState/tdk)).

## TypeScript[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#typescript)

- [Codelyzer](https://github.com/mgechev/codelyzer) - 一组 tslint 规则，用于 Angular 2 TypeScript 项目的静态代码分析.
- [ESLint](https://github.com/typescript-eslint/typescript-eslint) -TypeScript 语言的可扩展 linter.
- [tslint-clean-code](https://github.com/Glavin001/tslint-clean-code) - 受《清洁法规》手册启发的一组 TSLint 规则.
- [tslint-microsoft-contrib](https://github.com/Microsoft/tslint-microsoft-contrib) - 一组由 Microsoft 维护的 Typelin 项目的静态代码分析的 tslint 规则.

## VBScript[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#vbscript)

- [Test Design Studio](http://patterson-consulting.net/tds) ：copyright：- 具有静态代码分析功能的完整 IDE，用于 Micro Focus 统一功能测试基于 VBScript 的自动化测试.

## Multiple languages[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#multiple-languages)

- [AppChecker](https://npo-echelon.ru/en/solutions/appchecker.php) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Static analysis for C/C++/C#, PHP and Java
- [Application Inspector](https://www.ptsecurity.com/ww-en/products/ai/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Commercial Static Code Analysis which generates exploits to verify vulnerabilities. Supports: Java (including JSP and JSF), C#, VB.Net, ASP.NET, Php, JavaScript, Objective-C, Swift, C\C++, SQL (PL/SQL. T-SQL. MySQL), HTML5
- [ApplicationInspector](https://github.com/microsoft/ApplicationInspector) - creates reports of over 400 rule patterns for feature detection (e.g. the use of cryptography or version control in apps). Supports C/C++, C#, Java, JavaScript, HTML, Python, Objective-C, Go, Ruby, Powershell
- [AppScan Source](https://www.hcltechsw.com/wps/portal/products/appscan/home) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Commercial Static Code Analysis. Supports: Microsoft .NET Framework (C#, ASP.NET, VB.NET), ASP (JavaScript/VBScript), C/C++, COBOL, ColdFusion, JavaScript, JavaServer Pages (JSP), Java™ (including support for Android APIs), Perl, PHP, PL/SQL, T-SQL, Visual Basic 6
- [APPscreener](https://solarappscreener.com/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Static code analysis for binary and source code - Java/Scala, PHP, Javascript, C#, PL/SQL, Python, T-SQL, C/C++, ObjectiveC/Swift, Visual Basic 6.0, Ruby, Delphi, ABAP, HTML5 and Solidity
- [ArchUnit](https://www.archunit.org/) - 对 Java 或 Kotlin 架构进行单元测试
- [Atom-Beautify](https://atom.io/packages/atom-beautify) - Beautify HTML, CSS, JavaScript, PHP, Python, Ruby, Java, C, C++, C#, Objective-C, CoffeeScript, TypeScript, Coldfusion, SQL, and more in Atom editor
- [Axivion Bauhaus Suite](https://www.axivion.com/en/products-services-9#products_bauhaussuite) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Tracks down error-prone code locations, style violations, cloned or dead code, cyclic dependencies and more for C/C++, C#/.NET, Java and Ada 83/Ada 95
- [CAST Highlight](https://www.castsoftware.com/products/highlight) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Commercial Static Code Analysis which runs locally, but uploads the results to its cloud for presentation. Supports: Java, JavaScript, Python, JSP, COBOL, SAP/Abap, C/C++, C#, PHP, Visual Basic, T-SQL, PL/SQL.
- [Checkmarx CxSAST](https://www.checkmarx.com/products/static-application-security-testing/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Commercial Static Code Analysis which doesn't require pre-compilation. Supports: Android (Java), Apex and VisualForce, ASP, C#, C/C++, Go, Groovy, HTML5, Java, JavaScript, Node.js, Objective C, Perl, PhoneGap, PHP, Python, Ruby, Scala, Swift, VB.NET, VB6, VBScript
- [ClassGraph](https://github.com/classgraph/classgraph) - 用于查询或可视化类元数据或类相关性的类路径和模块路径扫描器. 支持 JVM 语言.
- [coala](https://coala.io/) - 用于创建代码分析的语言独立框架 - 支持 [over 60 languages](https://coala.io/languages) 默认
- [Cobra](http://spinroot.com/cobra/) ：copyright：-NASA 喷气推进实验室的结构源代码分析器. 支持 C，C ++，Ada 和 Python.
- [codeburner](https://github.com/groupon/codeburner) - 提供统一的界面来对发现的问题进行排序并采取行动
- [CodeFactor](https://codefactor.io/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Static Code Analysis for C#, C, C++, CoffeeScript, CSS, Groovy, GO, JAVA, JavaScript, Less, Python, Ruby, Scala, SCSS, TypeScript.
- [CodeIt.Right](https://submain.com/products/codeit.right.aspx) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - CodeIt.Right™ provides a fast, automated way to ensure that your source code adheres to (your) predefined design and style guidelines as well as best coding practices. Supported languages: C#, VB.NET.
- [CodeScene](https://empear.com/) ：copyright：-CodeScene 优先考虑技术债务，查找社会模式并识别代码中的隐患.
- [Coverity](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Synopsys Coverity supports 20 languages and over 70 frameworks including Ruby on rails, Scala, PHP, Python, JavaScript, TypeScript, Java, Fortran, C, C++, C#, VB.NET.
- [cqc](https://github.com/xcatliu/cqc) - 检查 js，jsx，vue，css，less，scss，sass 和 styl 文件的代码质量.
- [DeepCode](https://www.deepcode.ai/) ：copyright：-DeepCode 基于 AI 查找错误，安全漏洞，性能和 API 问题. DeepCode 的分析速度使我们能够实时分析您的代码并在您单击 IDE 中的 “保存” 按钮时提供结果. 支持的语言是 Java，C / C ++，JavaScript，Python 和 TypeScript. 与 GitHub，BitBucket 和 Gitlab 的集成.
- [DeepSource](https://deepsource.io/) ：copyright：- 深入的静态分析以监视源代码的质量和安全性. 支持 Python 和 Go，并且可以在错误风险，安全性，反模式，性能，文档和样式等垂直方面检测 600 多种类型的问题. 与 GitHub 的本机集成.
- [Depends](https://github.com/multilang-depends/depends) - 分析 Java，C / C ++，Ruby 的代码元素的全面依赖关系.
- [DevSkim](https://github.com/microsoft/devskim) - Regex-based static analysis tool for Visual Studio, VS Code, and Sublime Text - C/C++, C#, PHP, ASP, Python, Ruby, Java, and others.
- [Fortify](https://software.microfocus.com/en-us/products/static-code-analysis-sast/overview) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - A commercial static analysis platform that supports the scanning of C/C++, C#, VB.NET, VB6, ABAP/BSP, ActionScript, Apex, ASP.NET, Classic ASP, VB Script, Cobol, ColdFusion, HTML, Java, JS, JSP, MXML/Flex, Objective-C, PHP, PL/SQL, T-SQL, Python (2.6, 2.7), Ruby (1.9.3), Swift, Scala, VB, and XML.
- [Goodcheck](https://github.com/sideci/goodcheck) - 基于正则表达式的可定制棉短绒
- [graudit](https://github.com/wireghoul/graudit) - Grep rough audit - source code auditing tool - C/C++, PHP, ASP, C#, Java, Perl, Python, Ruby
- [Hound CI](https://houndci.com/) - 在 GitHub 拉取请求中评论样式违规. 支持 Coffeescript，Go，HAML，JavaScript，Ruby，SCSS 和 Swift.
- [imhotep](https://github.com/justinabrahms/imhotep) - 对提交到存储库中的提交进行评论，并检查语法错误和常规的掉毛警告.
- [Infer](https://github.com/facebook/infer) - 用于 Java，C 和 Objective-C 的静态分析器
- [InsiderSec](https://github.com/insidersec/insider) - A open source Static Application Security Testing tool (SAST) written in GoLang for Java (Maven and Android), Kotlin (Android), Swift (iOS), .NET Full Framework, C# and Javascript (Node.js).
- [Kiuwan](https://www.kiuwan.com/code-security-sast/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - Identify and remediate cyber threats in a blazingly fast, collaborative environment, with seamless integration in your SDLC. Python, C\C++, Java, C#, PHP and more
- [Klocwork](http://www.klocwork.com/products-services/klocwork) ：copyright：- 针对 C / C ++，Java 和 C 的质量和安全性静态分析#
- [oclint](https://github.com/oclint/oclint) - 静态源代码分析工具，可提高 C，C ++ 和 Objective-C 的质量并减少缺陷
- [pfff](https://github.com/facebook/pfff) -Facebook 用于多种语言的代码分析，可视化或保留样式源转换的工具
- [PMD](https://pmd.github.io/) -Java，Javascript，PLSQL，XML，XSL 等的源代码分析器
- [pre-commit](https://github.com/pre-commit/pre-commit) - 用于管理和维护多语言预提交挂钩的框架.
- [Pronto](https://github.com/prontolabs/pronto) - 快速自动代码审查您的更改. 支持 40 多种语言的跑步者，包括 Clang，Elixir，JavaSCript，PHP，Ruby 等
- [PT.PM](https://github.com/PositiveTechnologies/PT.PM) - An engine for searching patterns in the source code, based on Unified AST or UST. At present time C#, Java, PHP, PL/SQL, T-SQL, and JavaScript are supported. Patterns can be described within the code or using a DSL.
- [PVS-Studio](https://www.viva64.com/en/pvs-studio/) ：版权：-a（[conditionally free](https://www.viva64.com/en/b/0614/) for FOSS and individual developers) static analysis of C, C++, C# and Java code. For advertising purposes [you can propose a large FOSS project for analysis by PVS employees](https://github.com/viva64/pvs-studio-check-list) . 支持 CWE 映射，MISRA 和 CERT 编码标准.
- [Qualys Container Security](https://www.qualys.com/apps/container-security/) ：copyright：- 容器本机应用程序保护，以提供对容器化应用程序的可见性和控制.
- [Reviewdog](https://github.com/haya14busa/reviewdog) - 一种在任何代码托管服务中发布来自任何 linter 的评论评论的工具.
- [Security Code Scan](https://security-code-scan.github.io/) - Security code analyzer for C# and VB.NET. Detects various security vulnerability patterns: SQLi, XSS, CSRF, XXE, Open Redirect, etc.
- [Semmle QL and LGTM](https://semmle.com/) ：copyright：- 使用对源代码的查询来查找安全漏洞，变体和关键代码质量问题. 自动检查 PR 代码； 对于公共 GitHub / Bitbucket 回购免费： [LGTM.com](https://lgtm.com/).
- [shipshape](https://github.com/google/shipshape) - 静态程序分析平台，允许自定义分析仪通过通用接口插入
- [SmartDec Scanner](https://smartdecscanner.com/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - SAST tool which is capable of identifying vulnerabilities and undocumented features. The analyzer scans the source code and executables without debug info (i.e. binaries). Supports: Java/Scala/Kotlin, PHP, C#, JavaScript, TypeScript, VBScript, HTML5, Python, Perl, C/C++, Objective-C/Swift, PL/SQL, T-SQL, ABAP, 1C, Apex, Go, Ruby, Groovy, Delphi, VBA, Visual Basic 6, Solidity, Vyper, COBOL.
- [SonarQube](http://www.sonarqube.org/) -SonarQube 是管理代码质量的开放平台.
- [STOKE](https://github.com/StanfordPL/stoke) - 用于 x86_64 指令集的编程语言不可知随机优化器. 它使用随机搜索来探索所有可能的程序转换的极高维空间
- [Synopsys](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - A commercial static analysis platform that allows for scanning of multiple languages (C/C++, Android, C#, Java, JS, PHP, Python, Node.JS, Ruby, Fortran, and Swift)
- [TscanCode](https://github.com/Tencent/TscanCode) - A fast and accurate static analysis solution for C/C++, C#, Lua codes provided by Tencent. Using GPLv3 license.
- [Undebt](https://github.com/Yelp/undebt) - 基于语言的工具，可基于简单的模式定义进行大规模，自动，可编程的重构
- [Unibeautify](https://unibeautify.com/) - 带有 GitHub 应用的通用代码美化器. 支持 HTML，CSS，JavaScript，TypeScript，JSX，Vue，C ++，Go，Objective-C，Java，Python，PHP，GraphQL，Markdown 等.
- [Veracode](http://www.veracode.com/products/static-analysis-sast/static-code-analysis) ：copyright：- 在不需要源代码的情况下查找二进制文件和字节码中的缺陷. 支持所有主要的编程语言：Java，.NET，JavaScript，Swift，Objective-C，C，C ++ 等.
- [WALA](http://wala.sourceforge.net/wiki/index.php/Main_Page) -Java 字节码和相关语言以及 JavaScript 的静态分析功能
- [WhiteHat Application Security Platform](https://www.whitehatsec.com/products/static-application-security-testing/) ![©️](静态分析和代码质量- 超赞合集awesome list chinese.assets/00a9.svg) - WhiteHat Scout (for Developers) combined with WhiteHat Sentinel Source (for Operations) supporting WhiteHat Top 40 and OWASP Top 10. Language support for: Java, C#(.NET), ASP.NET, PHP, JavaScript, Node.js, Objective-C, Android, HTML5, TypeScript.
- [Wotan](https://github.com/fimbullinter/wotan) - Pluggable TypeScript and JavaScript linter
- [XCode](https://developer.apple.com/xcode/) ：copyright：-XCode 为 [Clang's](http://clang-analyzer.llvm.org/xcode.html) 静态代码分析器（C / C ++，Obj-C）

## Other[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#other)

## Binaries[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#binaries)

- [BinSkim](https://github.com/Microsoft/binskim) - 二进制静态分析工具，可为 Windows 可移植可执行文件提供安全性和正确性结果.
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) -cwe_checker 在二进制可执行文件中找到易受攻击的模式.
- [Jakstab](https://github.com/jkinder/jakstab) -Jakstab 是基于抽象解释的集成反汇编和静态分析框架，用于设计可执行文件的分析并恢复可靠的控制流程图.
- [Twiggy](https://github.com/rustwasm/twiggy) - Analyzes a binary's call graph to profile code size. The goal is to slim down binaries.

## Build tools[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#build-tools)

- [checkmake](https://github.com/mrtazz/checkmake) - 用于文件的分析器 / 分析器
- [codechecker](https://github.com/Ericsson/codechecker) -Clang 静态分析器的缺陷数据库和查看器扩展

## CSS/SASS/SCSS[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#csssassscss)

- [CSS Stats](https://github.com/cssstats/cssstats) - 样式表上可能有趣的统计信息
- [CSScomb](https://github.com/csscomb/csscomb.js) -CSS 的编码样式格式化程序. 支持自己的配置，使样式表美观且一致
- [CSSLint](https://github.com/CSSLint/csslint) - 是否进行基本语法检查并发现有问题的模式或效率低下的迹象
- [GraphMyCSS.com](https://graphmycss.com/) -CSS 特异性图生成器
- [Parker](https://github.com/katiefenn/parker) - 样式表分析工具
- [Project Wallace CSS Analyzer](https://github.com/projectwallace/css-analyzer) -CSS 的分析工具，属于 [Project Wallace](https://www.projectwallace.com/)
- [sass-lint](https://github.com/sasstools/sass-lint) - 适用于 sass 和 scss 语法的仅节点 Sass linter.
- [scsslint](https://github.com/brigade/scss-lint) -Sinter 文件的 Linter
- [Specificity Graph](https://github.com/pocketjoso/specificity-graph) -CSS 特异性图生成器
- [Stylelint](http://stylelint.io/) - 用于 SCSS / CSS 文件的 Linter

## Config Files[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#config-files)

- [dotenv-linter](https://github.com/wemake-services/dotenv-linter) - 像魅力一样整理 dotenv 文件.
- [gixy](https://github.com/yandex/gixy) - 分析 Nginx 配置的工具. 主要目标是防止配置错误并自动进行缺陷检测.

## Configuration Management[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#configuration-management)

- [ansible-lint](https://github.com/willthames/ansible-lint) - 检查剧本中可能会改善的做法和行为
- [cfn-lint](https://github.com/awslabs/cfn-python-lint) -AWS Labs CloudFormation linter.
- [cfn_nag](https://github.com/stelligent/cfn_nag) - 适用于 AWS CloudFormation 模板的模板.
- [checkov](https://github.com/bridgecrewio/checkov/) - 用于 Terraform 文件的静态分析工具（tf> = v0.12），可防止在构建时云配置错误.
- [cookstyle](https://docs.chef.io/cookstyle.html) -Cookstyle 是基于 RuboCop Ruby linting 工具的厨师工具整理工具
- [foodcritic](http://www.foodcritic.io/) - 检查主厨食谱中常见问题的皮棉工具.
- [Puppet Lint](https://github.com/rodjek/puppet-lint) - 检查您的人偶清单是否符合样式指南.
- [terraform-compliance](https://terraform-compliance.com/) - 针对 Terraform 的轻量级，专注于合规性和安全性的 BDD 测试框架.
- [terrascan](https://github.com/cesar-rodriguez/terrascan) - 收集用于 Terraform 模板的静态代码分析的安全性和最佳实践测试.
- [tflint](https://github.com/wata727/tflint) - 一种 Terraform linter，用于检测 “terraform plan” 无法检测到的错误.

## Containers[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#containers)

- [anchore](https://anchore.io/) - 发现，分析和验证容器映像
- [clair](https://github.com/coreos/clair) - 容器的漏洞静态分析
- [collector](https://github.com/banyanops/collector) - 在容器内运行任意脚本，并收集有用的信息
- [dagda](https://github.com/eliasgranderubio/dagda) - 对 Docker 映像 / 容器中的已知漏洞执行静态分析.
- [Docker Label Inspector](https://github.com/garethr/docker-label-inspector) - 整理和验证 Dockerfile 标签
- [Haskell Dockerfile Linter](https://github.com/lukasmartinelli/hadolint) - 更智能的 Dockerfile Linter，可帮助您构建最佳实践 Docker 映像
- [kube-score](https://github.com/zegl/kube-score) -Kubernetes 对象定义的静态代码分析.

## Gherkin[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#gherkin)

- [gherkin-lint](https://github.com/vsiakka/gherkin-lint) - 用 Java 语言编写的小黄瓜语法的短毛猫.

## HTML[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#html)

- [HTML Inspector](https://github.com/philipwalton/html-inspector) -HTML Inspector 是一种代码质量工具，可帮助您和您的团队编写更好的标记.
- [HTML Tidy](http://www.html-tidy.org/) - 通过修复标记错误并将旧代码升级为现代标准来纠正和清理 HTML 和 XML 文档.
- [HTMLHint](https://github.com/yaniswang/HTMLHint) - 用于 HTML 的静态代码分析工具
- [Polymer-analyzer](https://github.com/Polymer/polymer-analyzer) -Web 组件的静态分析框架.

## HTML5[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#html5)

- [HTML Inspector](https://github.com/philipwalton/html-inspector) -HTML Inspector 是一种代码质量工具，可帮助您和您的团队编写更好的标记.
- [HTML Tidy](http://www.html-tidy.org/) - 通过修复标记错误并将旧代码升级为现代标准来纠正和清理 HTML 和 XML 文档.
- [HTMLHint](https://github.com/yaniswang/HTMLHint) - 用于 HTML 的静态代码分析工具
- [Polymer-analyzer](https://github.com/Polymer/polymer-analyzer) -Web 组件的静态分析框架.

## IDE Plugins[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#ide-plugins)

- [ale](https://github.com/w0rp/ale) -Vim 和 NeoVim 的异步 Lint 引擎，支持多种语言
- [Android Studio](https://developer.android.com/studio) - 基于 IntelliJ IDEA，并捆绑了适用于 Android 的工具，包括 Android Lint.
- [Attackflow Extension](https://www.attackflow.com/Extension) - 用于 Visual Studio 的 Attackflow 插件，它使开发人员无需任何先验知识即可在源代码中实时发现关键的安全错误.
- [DevSkim](https://github.com/Microsoft/DevSkim) - 在线实时安全分析. 与多种编程语言和 IDE（VS，VS Code，Sublime Text 等）配合使用.
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - 捆绑了许多针对 Java 和 Kotlin 的检查，并包括用于重构，格式化等的工具.
- [Puma Scan](https://github.com/pumasecurity/puma-scan) - 开发团队在 Visual Studio 中编写代码时，Puma Scan 提供了针对常见漏洞（XSS，SQLi，CSRF，LDAPi，加密，反序列化等）的实时安全代码分析.
- [Security Code Scan](https://security-code-scan.github.io/) - Security code analyzer for C# and VB.NET that integrates into Visual Studio 2015 and newer. Detects various security vulnerability patterns: SQLi, XSS, CSRF, XXE, Open Redirect, etc.
- [vint](https://github.com/Kuniwak/vint) - 由 Python 实现的快速且高度可扩展的 Vim 脚本语言 Lint.

## LaTeX[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#latex)

- [ChkTeX](http://www.nongnu.org/chktex/) - 用于 LaTex 的短毛绒，它捕获 LaTeX 监督的一些印刷错误.
- [lacheck](https://www.ctan.org/pkg/lacheck) - 查找 LaTeX 文档中常见错误的工具.

## Makefiles[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#makefiles)

- [portlint](https://www.freebsd.org/cgi/man.cgi?query=portlint&sektion=1&manpath=FreeBSD+8.1-RELEASE+and+Ports) -FreeBSD 和 DragonFlyBSD 端口目录的验证程序.

## Markdown[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#markdown)

- [markdownlint](https://github.com/DavidAnson/markdownlint) - 用于 Markdown / CommonMark 文件的基于 Node.js 的样式检查器和 lint 工具.
- [mdl](https://github.com/mivok/markdownlint) - 检查 Markdown 文件和标志样式问题的工具.
- [remark-lint](https://github.com/remarkjs/remark-lint) - 用 JavaScript 编写的可插入 Markdown 代码样式的 linter.

## Mobile[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#mobile)

- [Android Lint](http://tools.android.com/tips/lint) - 在 Android 项目上运行静态分析.
- [android-lint-summary](https://github.com/passy/android-lint-summary) - 将多个项目的棉绒错误合并为一个输出，立即检查多个子项目的棉绒结果.
- [FlowDroid](https://github.com/secure-software-engineering/soot-infoflow-android) - static taint analysis tool for Android applications
- [paprika](https://github.com/GeoffreyHecht/paprika) - 一个工具包，用于检测已分析的 Android 应用程序中的某些代码气味.
- [qark](https://github.com/linkedin/qark) - 查找多个与安全性相关的 Android 应用程序漏洞的工具

## Packages[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#packages)

- [lintian](https://github.com/Debian/lintian) -Debian 软件包的静态分析工具
- [rpmlint](https://github.com/rpm-software-management/rpmlint) - 用于检查 rpm 包中常见错误的工具

## Protocol Buffers[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#protocol-buffers)

- [protolint](https://github.com/yoheimuta/protolint) - 可插入的 linter 和 fixer，用于实施协议缓冲区样式和约定.

## Supporting Tools[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#supporting-tools)

- [LibVCS4j](https://github.com/uni-bremen-agst/libvcs4j) - 一个 Java 库，通过为不同的版本控制系统和问题跟踪器提供通用 API，允许现有工具分析软件系统的演变.
- [Violations Lib](https://github.com/tomasbjerre/violations-lib) - Java library for parsing report files from static code analysis. Used by a bunch of Jenkins, Maven and Gradle plugins.

## Template-Languages[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#template-languages)

- [ember-template-lint](https://github.com/rwjblue/ember-template-lint) - 灰烬的 Ember 或 Handlebars 模板.
- [haml-lint](https://github.com/brigade/haml-lint) - 用于编写干净且一致的 HAML 的工具
- [slim-lint](https://github.com/sds/slim-lint) - 用于分析 Slim 模板的可配置工具
- [yamllint](https://github.com/adrienverge/yamllint) - 检查 YAML 文件的语法有效性，键重复和外观问题，例如行长，尾随空格和缩进.

## Translation[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#translation)

- [dennis](https://github.com/willkg/dennis/) - 一组用于处理 PO 文件的实用程序，以简化开发并提高质量.

## Web services[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#web-services)

- [Codacy](https://www.codacy.com/) - 代码分析可以更快地发布更好的代码.
- [Code Climate](https://codeclimate.com/) - 面向所有人的开放和可扩展的静态分析平台.
- [Code Inspector](https://www.code-inspector.com/) - 支持 10 多种语言的代码质量和技术债务管理平台.
- [Codeac](https://www.codeac.io/?ref=awesome-static-analysis) - 自动化的代码审查工具与 GitHub，Bitbucket 和 GitLab 集成（甚至是自托管）. 适用于 JavaScript，TypeScript，Python，Ruby，Go，PHP，Java，Docker 等. （免费开源）
- [CodeFactor](https://codefactor.io/) - 在 GitHub 或 BitBucket 上针对仓库的自动代码分析.
- [CodeFlow](https://www.getcodeflow.com/) - 自动代码分析工具，可处理技术深度. 与 Bitbucket 和 Gitlab 集成. （对于开源项目免费）
- [CodePatrol](https://cyber-security.claranet.fr/en/codepatrol) - 由安全性驱动的自动 SAST 代码检查，支持 15 种以上的语言，并包括安全培训.
- [Embold](https://embold.io/) - Intelligent software analytics platform that identifies design issues, code issues, duplication and metrics. Supports Java, C, C++, C#, JavaScript, TypeScript, Python, Go, Kotlin and more.
- [kiuwan](https://www.kiuwan.com/) - 云中的软件分析，支持超过 22 种编程语言.
- [Landscape](https://landscape.io/) -Python 的静态代码分析
- [LGTM.com](https://lgtm.com/) - 针对 GitHub 和 Bitbucket 的深入代码分析，以发现安全漏洞和关键代码质量问题（使用 Semmle QL）. 自动查看拉取请求的代码； 免费用于公共存储库.
- [Nitpick CI](https://nitpick-ci.com/) - 自动化的 PHP 代码审查
- [PullRequest](https://www.pullrequest.com/) - 将代码审查作为具有内置静态分析的服务
- [QuantifiedCode](https://www.quantifiedcode.com/) - 自动代码审查和修复
- [Reshift](https://softwaresecured.com/reshift/) - 用于检测和管理 Java 安全漏洞的源代码分析工具.
- [Scrutinizer](https://scrutinizer-ci.com/) - 可以与 GitHub 集成的专有代码质量检查器
- [SensioLabs Insight](https://insight.sensiolabs.com/) - 检测安全风险，发现错误并为 PHP 项目提供可行的指标
- [Sider](https://sider.review/) - 自动代码检查工具. 提高开发人员的生产力.
- [Snyk](https://snyk.io/) - 漏洞扫描程序，用于依赖 node.js 应用程序（开放源代码项目免费）
- [SonarCloud](https://sonarcloud.io/) - 基于多语言云的静态代码分析. 历史，趋势，安全热点，请求请求分析等. 免费提供开源.
- [Teamscale](http://www.teamscale.com/) - 静态和动态分析工具，支持超过 25 种语言并直接集成了 IDE. 可应要求免费托管开源项目. 提供免费的学术许可证.
- [Upsource](https://www.jetbrains.com/upsource/) - 具有 Java，PHP，JavaScript 和 Kotlin 的静态代码分析和代码感知导航的代码审查工具.

## Writing[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#writing)

- [After the Deadline](https://afterthedeadline.com/) - 拼写，样式和语法检查器
- [codespell](https://github.com/codespell-project/codespell) - 检查常见拼写错误的代码
- [languagetool](https://github.com/languagetool-org/languagetool) - 超过 25 种语言的样式和语法检查器. 它会发现许多简单的拼写检查器无法检测到的错误.
- [misspell-fixer](https://github.com/vlajos/misspell-fixer) - 在源代码中修复常见拼写错误，错别字的快速工具
- [Misspelled Words In Context](https://github.com/jwilk/mwic) - 拼写检查器，对可能的拼写错误进行分组并在上下文中显示它们
- [proselint](https://github.com/amperser/proselint/) - 专为英语散文而设的短篇小说，重点是写作风格而不是语法.
- [vale](https://github.com/ValeLint/vale) - 用于散文的可自定义，语法感知的 linter.
- [write-good](https://github.com/btford/write-good) - 重点消除 “狡猾的单词” 的短毛猫.

## More collections[¶](https://asmcn.icopy.site/awesome/awesome-static-analysis/#more-collections)

- [go-tools](https://github.com/dominikh/go-tools) - 使用 Go 代码的工具和库的集合，包括短绒和静态分析
- [linters](https://github.com/mcandre/linters) - 静态代码分析简介
- [php-static-analysis-tools](https://github.com/exakat/php-static-analysis-tools) - 有用的 PHP 静态分析工具的完整列表
- [Wikipedia](http://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis) - 用于静态代码分析的工具列表.