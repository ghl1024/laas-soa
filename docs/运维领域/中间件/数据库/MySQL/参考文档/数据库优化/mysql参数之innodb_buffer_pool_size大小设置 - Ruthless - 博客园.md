```
用于缓存索引和数据的内存大小，这个当然是越多越好， 数据读写在内存中非常快， 减少了对磁盘的读写。 当数据提交或满足检查点条件后才一次性将内存数据刷新到磁盘中。然而内存还有操作系统或数据库其他进程使用， 根据经验，推荐设置innodb-buffer-pool-size为服务器总可用内存的75%。 若设置不当， 内存使用可能浪费或者使用过多。 对于繁忙的服务器， buffer pool 将划分为多个实例以提高系统并发性， 减少线程间读写缓存的争用。buffer pool 的大小首先受 innodb_buffer_pool_instances 影响， 当然影响较小。

Innodb_buffer_pool_pages_data
Innodb buffer pool缓存池中包含数据的页的数目，包括脏页。单位是page。
eg、show global status like 'Innodb_buffer_pool_pages_data';

  
Innodb_buffer_pool_pages_total
innodb buffer pool的页总数目。单位是page。
eg：show global status like 'Innodb_buffer_pool_pages_total';

show global status like 'Innodb_page_size';

查看@@innodb_buffer_pool_size大小，单位字节
SELECT @@innodb_buffer_pool_size/1024/1024/1024; #字节转为G

在线调整InnoDB缓冲池大小，如果不设置，默认为128M
set global innodb_buffer_pool_size = 4227858432; ##单位字节

计算Innodb_buffer_pool_pages_data/Innodb_buffer_pool_pages_total*100%
当结果 > 95% 则增加 innodb_buffer_pool_size， 建议使用物理内存的 75%
当结果 < 95% 则减少 innodb_buffer_pool_size， 
建议设置大小为： Innodb_buffer_pool_pages_data * Innodb_page_size * 1.05 / (1024*1024*1024)
```

