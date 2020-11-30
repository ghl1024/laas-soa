查看dirty_page比例:

show variables like '%innodb_max_dirty_pages_pct%';



+------------------------------+-----------+

| Variable_name                 | Value     |
+------------------------------+-----------+
| innodb_max_dirty_pages_pct     | 60.000000 |
| innodb_max_dirty_pages_pct_lwm | 1.000000  |
+------------------------------+-----------+

查看脏页的深度
show variables like '%innodb_lru_scan_depth%';

+---------------------+-------+
| Variable_name        | Value |
+---------------------+-------+
| innodb_lru_scan_depth | 2048  |
+---------------------+-------+

写入量
show variables like '%innodb_io_capacity%';
+----------------------+-------+
| Variable_name         | Value |
+----------------------+-------+
| innodb_io_capacity     | 4000  |
| innodb_io_capacity_max | 8000  |



show variables like '%innodb_buffer_pool_size%';

+----------------------+-------------+
| Variable_name         | Value       |
+----------------------+-------------+
| innodb_buffer_pool_size | 25769803776 |
+----------------------+-------------+
目前24G

show variables like '%innodb_log_file_size%';

+-------------------+------------+
| Variable_name      | Value      |
+-------------------+------------+
| innodb_log_file_size | 1073741824 |
+-------------------+------------+
目前为1G

show variables like '%innodb_flush_method%';

目前脏页比例过低, 建议加到90
innodb_io_capacity *2
innodb_io_capacity_max *2
innodb_log_file_size *2

对应修改polardb配置:
innodb_io_capacity: 8000
innodb_io_capacity_max: 16000
innodb_max_undo_log_size: 2147483648