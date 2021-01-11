[MySQL 8.0参考手册](https://dev.mysql.com/doc/refman/8.0/en/) / [...](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html) / EXPLAIN输出格式

### 8.8.2说明输出格式

该[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)语句提供有关MySQL如何执行语句的信息。 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)作品有 [`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)， [`DELETE`](https://dev.mysql.com/doc/refman/8.0/en/delete.html)， [`INSERT`](https://dev.mysql.com/doc/refman/8.0/en/insert.html)， [`REPLACE`](https://dev.mysql.com/doc/refman/8.0/en/replace.html)，和 [`UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/update.html)语句。

[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)为[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)语句中使用的每个表返回一行信息 。它按照MySQL在处理语句时读取它们的顺序列出了输出中的表。这意味着MySQL从第一个表中读取一行，然后在第二个表中然后在第三个表中找到匹配的行，依此类推。处理完所有表后，MySQL将通过表列表输出选定的列和回溯，直到找到一个表，其中存在更多匹配的行。从该表中读取下一行，然后继续下一个表。

注意

MySQL Workbench具有视觉解释功能，可提供[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)输出的视觉表示 。请参见 [教程：使用解释来提高查询性能](https://dev.mysql.com/doc/workbench/en/wb-tutorial-visual-explain-dbt3.html)。

- [解释输出列](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-output-columns)
- [解释联接类型](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-join-types)
- [了解更多信息](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-extra-information)
- [解释输出解释](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-output-interpretation)

#### 解释输出列

本节描述产生的输出列 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。后面的部分提供有关[`type`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-join-types) 和 [`Extra`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-extra-information) 列的其他信息 。

的每个输出行[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html) 提供有关一个表的信息。每行包含[表8.1“ EXPLAIN输出列”中](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-output-column-table)概述的值 ，并在表后更详细地描述。列名显示在表的第一列中；第二列提供`FORMAT=JSON`使用时输出中显示的等效属性名称 。



**表8.1 EXPLAIN输出列**

| 柱                                                           | JSON名称        | 含义                   |
| :----------------------------------------------------------- | :-------------- | :--------------------- |
| [`id`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_id) | `select_id`     | 该`SELECT`标识符       |
| [`select_type`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_select_type) | 没有            | 该`SELECT`类型         |
| [`table`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_table) | `table_name`    | 输出行表               |
| [`partitions`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_partitions) | `partitions`    | 匹配的分区             |
| [`type`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_type) | `access_type`   | 联接类型               |
| [`possible_keys`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_possible_keys) | `possible_keys` | 可能的索引选择         |
| [`key`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_key) | `key`           | 实际选择的索引         |
| [`key_len`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_key_len) | `key_length`    | 所选键的长度           |
| [`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_ref) | `ref`           | 与索引比较的列         |
| [`rows`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_rows) | `rows`          | 估计要检查的行         |
| [`filtered`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_filtered) | `filtered`      | 按表条件过滤的行百分比 |
| [`Extra`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain_extra) | 没有            | 附加信息               |



注意

`NULL`不会在JSON格式的`EXPLAIN` 输出中显示的 JSON属性。

- `id`（JSON名： `select_id`）

  的[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)标识符。这是[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)查询中的序号 。`NULL`如果该行引用其他行的并集结果，则该值为。在这种情况下，该 `table`列显示的值类似于 表明该行是指行的并集值为 和的并集 。 `<union*`M`*,*`N`*>``id`*`M`**`N`*

- `select_type` （JSON名称：无）

  的类型[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)，可以是下表中显示的任何类型。JSON格式的`EXPLAIN`公开 `SELECT`类型为a的属性 `query_block`，除非它为 `SIMPLE`或`PRIMARY`。表格中还显示了JSON名称（如果适用）。

  | `select_type` 值                                             | JSON名称                     | 含义                                                         |
  | :----------------------------------------------------------- | :--------------------------- | :----------------------------------------------------------- |
  | `SIMPLE`                                                     | 没有                         | 简单[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)（不使用 [`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html)或子查询） |
  | `PRIMARY`                                                    | 没有                         | 最外层 [`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html) |
  | [`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html) | 没有                         | [`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)陈述中的第二个或之后的陈述 [`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html) |
  | `DEPENDENT UNION`                                            | `dependent`（`true`）        | 中的第二个或更高版本的[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)语句 [`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html)，取决于外部查询 |
  | `UNION RESULT`                                               | `union_result`               | 的结果[`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html)。 |
  | [`SUBQUERY`](https://dev.mysql.com/doc/refman/8.0/en/optimizer-hints.html#optimizer-hints-subquery) | 没有                         | 首先[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)在子查询 |
  | `DEPENDENT SUBQUERY`                                         | `dependent`（`true`）        | 首先[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)在子查询中，取决于外部查询 |
  | `DERIVED`                                                    | 没有                         | 派生表                                                       |
  | `DEPENDENT DERIVED`                                          | `dependent`（`true`）        | 派生表依赖于另一个表                                         |
  | `MATERIALIZED`                                               | `materialized_from_subquery` | 物化子查询                                                   |
  | `UNCACHEABLE SUBQUERY`                                       | `cacheable`（`false`）       | 子查询，其结果无法缓存，必须针对外部查询的每一行重新进行评估 |
  | `UNCACHEABLE UNION`                                          | `cacheable`（`false`）       | [`UNION`](https://dev.mysql.com/doc/refman/8.0/en/union.html) 属于不可缓存子查询的中的第二个或更高版本的选择（请参阅参考资料 `UNCACHEABLE SUBQUERY`） |

  

  `DEPENDENT`通常表示使用相关子查询。请参见 [第13.2.11.7节“相关子查询”](https://dev.mysql.com/doc/refman/8.0/en/correlated-subqueries.html)。

  `DEPENDENT SUBQUERY`评估不同于`UNCACHEABLE SUBQUERY`评估。对于`DEPENDENT SUBQUERY`，子查询仅针对其外部上下文中变量的每组不同值重新评估一次。对于 `UNCACHEABLE SUBQUERY`，将为外部上下文的每一行重新评估子查询。

  当您指定`FORMAT=JSON`with时 `EXPLAIN`，输出没有直接等同于`select_type`;的单个属性 。该 `query_block`属性对应于给定`SELECT`。相当于大部分的性质`SELECT`只是示出子查询类型是可用的（一个例子是 `materialized_from_subquery`用于 `MATERIALIZED`），并且当被显示为宜。没有`SIMPLE`或的JSON等效项 `PRIMARY`。

  `select_type`非[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)语句 的值显示受影响表的语句类型。例如，`select_type`是 `DELETE`对 [`DELETE`](https://dev.mysql.com/doc/refman/8.0/en/delete.html)报表。

- `table`（JSON名： `table_name`）

  输出行所引用的表的名称。这也可以是以下值之一：

  - `<union*`M`*,*`N`*>`：该行是指具有和`id`值的行 的 *`M`*并集 *`N`*。
  - `<derived*`N`*>`：该行是指用于与该行的派生表结果`id`的值 *`N`*。派生表可能来自（例如）`FROM`子句中的子查询 。
  - `<subquery*`N`*>`：该行是指该行的物化子查询的结果，其`id` 值为*`N`*。请参见 [第8.2.2.2节“通过实现来优化子查询”](https://dev.mysql.com/doc/refman/8.0/en/subquery-materialization.html)。

- `partitions`（JSON名： `partitions`）

  查询将从中匹配记录的分区。该值适用`NULL`于未分区的表。请参见 [第24.3.5节“获取有关分区的信息”](https://dev.mysql.com/doc/refman/8.0/en/partitioning-info.html)。

- `type`（JSON名： `access_type`）

  联接类型。有关不同类型的描述，请参见 [`EXPLAIN` 连接类型](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-join-types)。

- `possible_keys`（JSON名： `possible_keys`）

  该`possible_keys`列指示MySQL可以选择从中查找表中各行的索引。请注意，此列完全独立于表的顺序，如的输出所示 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。这意味着`possible_keys`在实践中，某些键可能无法与生成的表顺序一起使用。

  如果此列是`NULL`（或在JSON格式的输出中未定义），则没有相关的索引。在这种情况下，您可以通过检查该`WHERE` 子句以检查它是否引用了某些适合索引的列，从而提高查询性能。如果是这样，请创建一个适当的索引并[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)再次检查查询 。请参见 [第13.1.9节“ ALTER TABLE语句”](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)。

  要查看表具有哪些索引，请使用。 `SHOW INDEX FROM *`tbl_name`*`

- `key`（JSON名：`key`）

  该`key`列指示MySQL实际决定使用的键（索引）。如果MySQL决定使用`possible_keys` 索引之一来查找行，则将该索引列为键值。

  可能`key`会命名值中不存在的索引 `possible_keys`。如果没有`possible_keys`索引适合查找行，但是查询选择的所有列都是其他索引的列，则会发生这种情况。也就是说，命名索引覆盖了选定的列，因此尽管不使用索引来确定要检索的行，但索引扫描比数据行扫描更有效。

  对于`InnoDB`，即使查询还选择了主键，辅助索引也可能覆盖选定的列，因为`InnoDB`主键值与每个辅助索引一起存储。如果 `key`为`NULL`，则MySQL没有找到可用于更有效地执行查询的索引。

  要强制MySQL使用或忽略列出的索引 `possible_keys`列，使用 `FORCE INDEX`，`USE INDEX`或`IGNORE INDEX`在您的查询。请参见[第8.9.4节“索引提示”](https://dev.mysql.com/doc/refman/8.0/en/index-hints.html)。

  对于`MyISAM`表，运行 [`ANALYZE TABLE`](https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html)有助于优化器选择更好的索引。对于 `MyISAM`表，[**myisamchk --analyze也是**](https://dev.mysql.com/doc/refman/8.0/en/myisamchk.html)如此。请参见 [第13.7.3.1节“ ANALYZE TABLE语句”](https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html)和 [第7.6节“ MyISAM表维护和崩溃恢复”](https://dev.mysql.com/doc/refman/8.0/en/myisam-table-maintenance.html)。

- `key_len`（JSON名： `key_length`）

  该`key_len`列指示MySQL决定使用的密钥的长度。的值 `key_len`使您能够确定MySQL实际使用的多部分键的多少部分。如果该`key`列显示 `NULL`，则该`key_len` 列也显示`NULL`。

  由于密钥存储格式的原因，可以使用的列的密钥长度`NULL` 比使用`NOT NULL`列的密钥长度大一。

- `ref`（JSON名：`ref`）

  该`ref`列显示将哪些列或常量与该`key`列中命名的索引进行比较，以 从表中选择行。

  如果值为`func`，则使用的值是某些函数的结果。要查看哪个功能，请使用 [`SHOW WARNINGS`](https://dev.mysql.com/doc/refman/8.0/en/show-warnings.html)以下 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)命令查看扩展 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)输出。该函数实际上可能是算术运算符之类的运算符。

- `rows`（JSON名： `rows`）

  该`rows`列表示MySQL认为执行查询必须检查的行数。

  对于[`InnoDB`](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html)表，此数字是估计值，可能并不总是准确的。

- `filtered`（JSON名： `filtered`）

  该`filtered`列指示按表条件过滤的表行的估计百分比。最大值为100，这表示未过滤行。值从100减小表示过滤量增加。 `rows`显示了检查的估计行数，`rows`× `filtered`显示了与下表连接的行数。例如，如果 `rows`为1000且 `filtered`为50.00（50％），则与下表连接的行数为1000×50％= 500。

- `Extra` （JSON名称：无）

  此列包含有关MySQL如何解析查询的其他信息。有关不同值的说明，请参见“ [`EXPLAIN` 额外信息”](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#explain-extra-information)。

  该`Extra`列没有对应的JSON属性 ；但是，此列中可能出现的值显示为JSON属性或该`message`属性的文本。

#### 解释联接类型

该`type`列 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)输出介绍如何联接表。在JSON格式的输出中，这些作为`access_type`属性的值找到。以下列表描述了连接类型，从最佳类型到最差类型：

- [`system`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_system)

  

  

  

  该表只有一行（=系统表）。这是[`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)联接类型的特例 。

- [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)

  

  

  

  该表最多具有一个匹配行，该行在查询开始时读取。因为只有一行，所以优化器的其余部分可以将这一行中列的值视为常量。 [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)表非常快，因为它们只能读取一次。

  [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)在将a`PRIMARY KEY`或 `UNIQUE`index的所有部分与常量值进行比较时使用。在以下查询中，*`tbl_name`*可以用作[`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const) 表：

  ```sql
  SELECT * FROM tbl_name WHERE primary_key=1;
  
  SELECT * FROM tbl_name
    WHERE primary_key_part1=1 AND primary_key_part2=2;
  ```

- [`eq_ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_eq_ref)

  

  

  对于先前表中的每行组合，从此表中读取一行。除了 [`system`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_system)和 [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)类型，这是最好的联接类型。当连接使用索引的所有部分且索引为a `PRIMARY KEY`或`UNIQUE NOT NULL`index时使用。

  [`eq_ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_eq_ref)可以用于使用`=`运算符进行比较的索引列 。比较值可以是常量，也可以是使用在此表之前读取的表中列的表达式。在以下示例中，MySQL可以使用 [`eq_ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_eq_ref)联接进行处理 *`ref_table`*：

  ```sql
  SELECT * FROM ref_table,other_table
    WHERE ref_table.key_column=other_table.column;
  
  SELECT * FROM ref_table,other_table
    WHERE ref_table.key_column_part1=other_table.column
    AND ref_table.key_column_part2=1;
  ```

- [`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref)

  

  

  对于先前表中的每个行组合，将从该表中读取具有匹配索引值的所有行。[`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref)如果联接仅使用键的最左前缀，或者如果键不是a`PRIMARY KEY`或 `UNIQUE`index（换句话说，如果联接无法根据键值选择单个行），则使用。如果使用的键仅匹配几行，则这是一种很好的联接类型。

  [`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref)可以用于使用`=`或`<=>` 运算符进行比较的索引列 。在以下示例中，MySQL可以使用 [`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref)联接进行处理 *`ref_table`*：

  ```sql
  SELECT * FROM ref_table WHERE key_column=expr;
  
  SELECT * FROM ref_table,other_table
    WHERE ref_table.key_column=other_table.column;
  
  SELECT * FROM ref_table,other_table
    WHERE ref_table.key_column_part1=other_table.column
    AND ref_table.key_column_part2=1;
  ```

- [`fulltext`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_fulltext)

  

  

  使用`FULLTEXT` 索引执行联接。

- [`ref_or_null`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref_or_null)

  

  

  这种连接类型类似于 [`ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref)，但是除了MySQL还会额外搜索包含`NULL`值的行。此联接类型优化最常用于解析子查询。在以下示例中，MySQL可以使用 [`ref_or_null`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_ref_or_null)联接进行处理*`ref_table`*：

  ```sql
  SELECT * FROM ref_table
    WHERE key_column=expr OR key_column IS NULL;
  ```

  请参见[第8.2.1.15节“ IS NULL优化”](https://dev.mysql.com/doc/refman/8.0/en/is-null-optimization.html)。

- [`index_merge`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index_merge)

  

  

  此联接类型指示使用索引合并优化。在这种情况下，`key`输出行中的列包含使用的索引列表，并`key_len`包含使用的索引 的最长键部分的列表。有关更多信息，请参见 [第8.2.1.3节“索引合并优化”](https://dev.mysql.com/doc/refman/8.0/en/index-merge-optimization.html)。

- [`unique_subquery`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_unique_subquery)

  

  

  此类型替换 以下形式的[`eq_ref`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_eq_ref)某些 `IN`子查询：

  ```sql
  value IN (SELECT primary_key FROM single_table WHERE some_expr)
  ```

  [`unique_subquery`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_unique_subquery) 只是一个索引查找函数，它完全替代了子查询以提高效率。

- [`index_subquery`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index_subquery)

  

  

  此连接类型类似于 [`unique_subquery`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_unique_subquery)。它替代`IN`子查询，但适用于以下形式的子查询中的非唯一索引：

  ```sql
  value IN (SELECT key_column FROM single_table WHERE some_expr)
  ```

- [`range`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_range)

  

  

  使用索引选择行，仅检索给定范围内的行。的`key` 输出行中的列指示使用哪个索引。将`key_len`包含已使用的时间最长的关键部分。该`ref`列 `NULL`适用于此类型。

  [`range`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_range)当一个键列使用任何的相比于恒定可使用 [`=`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_equal)， [`<>`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_not-equal)， [`>`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_greater-than)， [`>=`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_greater-than-or-equal)， [`<`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_less-than)， [`<=`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_less-than-or-equal)， [`IS NULL`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_is-null)， [`<=>`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_equal-to)， [`BETWEEN`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_between)， [`LIKE`](https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html#operator_like)，或 [`IN()`](https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html#operator_in)运营商：

  ```sql
  SELECT * FROM tbl_name
    WHERE key_column = 10;
  
  SELECT * FROM tbl_name
    WHERE key_column BETWEEN 10 and 20;
  
  SELECT * FROM tbl_name
    WHERE key_column IN (10,20,30);
  
  SELECT * FROM tbl_name
    WHERE key_part1 = 10 AND key_part2 IN (10,20,30);
  ```

- [`index`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index)

  

  

  该`index`联接类型是一样的 [`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)，只是索引树被扫描。这发生两种方式：

  - 如果索引是查询的覆盖索引，并且可用于满足表中所需的所有数据，则仅扫描索引树。在这种情况下，`Extra`列显示为 `Using index`。仅索引扫描通常比索引扫描更快， [`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)因为索引的大小通常小于表数据。
  - 使用对索引的读取执行全表扫描，以按索引顺序查找数据行。 `Uses index`没有出现在 `Extra`列中。

  当查询仅使用属于单个索引一部分的列时，MySQL可以使用此联接类型。

- [`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)

  

  

  对来自先前表的行的每个组合进行全表扫描。如果该表是未标记的第一个表 [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)，则通常不好，并且在所有其他情况下通常 *非常*糟糕。通常，可以[`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)通过添加索引来避免这种情况，这些 索引允许基于早期表的常量值或列值从表中检索行。

#### 了解更多信息

该`Extra`列 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)输出包含MySQL解决查询的额外信息。以下列表说明了可以在此列中显示的值。每个项目还针对JSON格式的输出指示哪个属性显示`Extra`值。对于其中一些，有一个特定的属性。其他显示为`message` 属性的文本。

如果你想使你的查询尽可能快，看出来`Extra`的列值`Using filesort`和`Using temporary`，或在JSON格式的`EXPLAIN`输出，用于 `using_filesort`和 `using_temporary_table`性能等于 `true`。

- `Child of '*`table`*' pushed join@1`（JSON：`message` 文本）

  将该表引用为 *`table`*可以下推到NDB内核的联接中的子级。启用下推联接时，仅适用于NDB群集。有关[`ndb_join_pushdown`](https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-options-variables.html#sysvar_ndb_join_pushdown)更多信息和示例，请参见服务器系统变量的描述 。

- `const row not found`（JSON属性： `const_row_not_found`）

  对于诸如之类的查询，该表为空。 `SELECT ... FROM *`tbl_name`*`

- `Deleting all rows`（JSON属性： `message`）

  对于[`DELETE`](https://dev.mysql.com/doc/refman/8.0/en/delete.html)，某些存储引擎（如[`MyISAM`](https://dev.mysql.com/doc/refman/8.0/en/myisam-storage-engine.html)）支持一种处理程序方法，该方法以一种简单而快速的方式删除所有表行。`Extra`如果引擎使用此优化，则显示此值。

- `Distinct`（JSON属性： `distinct`）

  MySQL正在寻找不同的值，因此在找到第一个匹配的行后，它将停止为当前行组合搜索更多行。

- `FirstMatch(*`tbl_name`*)` （JSON属性：`first_match`）

  半联接FirstMatch联接快捷方式策略用于*`tbl_name`*。

- `Full scan on NULL key`（JSON属性： `message`）

  当优化器无法使用索引查找访问方法时，这将作为子查询优化的后备策略发生。

- `Impossible HAVING`（JSON属性： `message`）

  该`HAVING`子句始终为false，无法选择任何行。

- `Impossible WHERE`（JSON属性： `message`）

  该`WHERE`子句始终为false，无法选择任何行。

- `Impossible WHERE noticed after reading const tables`（JSON属性： `message`）

  MySQL已经读取了所有 [`const`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_const)（和 [`system`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_system)）表，并注意到该`WHERE`子句始终为false。

- `LooseScan(*`m`*..*`n`*)` （JSON属性：`message`）

  使用半连接的LooseScan策略。 *`m`*和 *`n`*是关键部件号。

- `No matching min/max row`（JSON属性： `message`）

  没有行满足查询的条件，例如 。 `SELECT MIN(...) FROM ... WHERE *`condition`*`

- `no matching row in const table`（JSON属性：`message`）

  对于具有联接的查询，存在一个空表或没有满足唯一索引条件的行的表。

- `No matching rows after partition pruning`（JSON属性： `message`）

  对于[`DELETE`](https://dev.mysql.com/doc/refman/8.0/en/delete.html)或 [`UPDATE`](https://dev.mysql.com/doc/refman/8.0/en/update.html)，在分区修剪后，优化器未发现任何要删除或更新的内容。它的含义类似于`Impossible WHERE` for[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)语句。

- `No tables used`（JSON属性： `message`）

  查询没有`FROM`子句，或者有 `FROM DUAL`子句。

  对于[`INSERT`](https://dev.mysql.com/doc/refman/8.0/en/insert.html)或 [`REPLACE`](https://dev.mysql.com/doc/refman/8.0/en/replace.html)语句， [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)在没有任何[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html) 部分时显示此值。例如，出现的`EXPLAIN INSERT INTO t VALUES(10)`原因是，它等同于 `EXPLAIN INSERT INTO t SELECT 10 FROM DUAL`。

- `Not exists`（JSON属性： `message`）

  MySQL能够对`LEFT JOIN` 查询进行优化，并且在找到符合`LEFT JOIN`条件的一行后，不再检查该表中的更多行是否为上一行。这是可以通过这种方式优化的查询类型的示例：

  ```sql
  SELECT * FROM t1 LEFT JOIN t2 ON t1.id=t2.id
    WHERE t2.id IS NULL;
  ```

  假设`t2.id`定义为 `NOT NULL`。在这种情况下，MySQL使用的值 扫描 `t1`并查找行 。如果MySQL在中找到匹配的行 ，它将知道它 永远不会是 ，并且不会扫描具有相同值的其余行。换句话说，对于in中的每一行，MySQL只需进行一次查找，无论in中实际匹配多少行。 `t2``t1.id``t2``t2.id``NULL``t2``id``t1``t2``t2`

  在MySQL 8.0.17及更高版本中，这还可以指示`WHERE`形式为的 条件 或 已在内部转换为反联接的条件。这将删除子查询，并将其表放入最顶层查询的计划中，从而改善了成本计划。通过合并半联接和反联接，优化器可以更自由地对执行计划中的表进行重新排序，在某些情况下，可以使计划更快。 `NOT IN (*`subquery`*)``NOT EXISTS (*`subquery`*)`

  通过检查或 执行的结果后 的`Message`列，您可以查看何时对给定查询执行反联接转换 。 `SHOW WARNINGS``EXPLAIN``EXPLAIN FORMAT=TREE`

  注意

  反连接是半连接的补充 。反联接返回所有行 ，其中 *没有*匹配的 行 。 `*`table_a`* JOIN *`table_b`* ON *`condition`*`*`table_a`**`table_b`**`condition`*

- `Plan isn't ready yet` （JSON属性：无）

  [`EXPLAIN FOR CONNECTION`](https://dev.mysql.com/doc/refman/8.0/en/explain-for-connection.html)当优化器尚未完成为在命名连接中执行的语句创建执行计划时， 就会出现此值。如果执行计划输出包括多行，则`Extra`取决于优化程序确定完整执行计划的进度，其中任何一行或所有行都可以具有此 值。

- `Range checked for each record (index map: *`N`*)`（JSON属性： `message`）

  MySQL找不到很好的索引来使用，但是发现一些索引可以在已知先前表中的列值之后使用。对于上表中的每个行组合，MySQL检查是否可以使用[`range`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_range)或 [`index_merge`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index_merge)访问方法来检索行。这不是很快，但是比根本没有索引的联接要快。适用条件如 [第8.2.1.2节“范围优化”](https://dev.mysql.com/doc/refman/8.0/en/range-optimization.html)和 [第8.2.1.3节“索引合并优化”中所述](https://dev.mysql.com/doc/refman/8.0/en/index-merge-optimization.html)，除了上表的所有列值都是已知的并且被视为常量。

  索引从1开始编号，其顺序[`SHOW INDEX`](https://dev.mysql.com/doc/refman/8.0/en/show-index.html)与表中显示的顺序相同。索引图值 *`N`*是指示哪些索引为候选的位掩码值。例如，`0x19`（二进制11001）的值表示考虑了索引1、4和5。

- `Recursive`（JSON属性： `recursive`）

  这表明该行适用于[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)递归公用表表达式的递归 部分。请参见[第13.2.15节“ WITH（公用表表达式）”](https://dev.mysql.com/doc/refman/8.0/en/with.html)。

- `Rematerialize`（JSON属性： `rematerialize`）

  

  

  `Rematerialize (X,...)`在`EXPLAIN`table的行中 显示`T`，其中`X`是任何横向派生的表，当`T`读取新行时会触发其重新实现。例如：

  ```sql
  SELECT
    ...
  FROM
    t,
    LATERAL (derived table that refers to t) AS dt
  ...
  ```

  每当`t`顶级查询处理新的一行时，都会重新实现派生表的内容，以使其保持最新状态 。

- `Scanned *`N`* databases`（JSON属性： `message`）

  这表明在处理`INFORMATION_SCHEMA`表查询时服务器执行了多少目录扫描 ，如[第8.2.3节“优化INFORMATION_SCHEMA查询”中所述](https://dev.mysql.com/doc/refman/8.0/en/information-schema-optimization.html)。的值*`N`*可以是0、1或 `all`。

- `Select tables optimized away`（JSON属性：`message`）

  优化器确定1）最多应返回一行，以及2）要生成该行，必须读取确定的一组行。当在优化阶段可以读取要读取的行时（例如，通过读取索引行），则在查询执行期间无需读取任何表。

  当查询被隐式分组（包含聚合函数但没有`GROUP BY`子句）时，满足第一个条件 。当使用的每个索引执行一次行查找时，满足第二个条件。读取的索引数确定要读取的行数。

  考虑以下隐式分组查询：

  ```sql
  SELECT MIN(c1), MIN(c2) FROM t1;
  ```

  假设`MIN(c1)`可以通过读取一个索引行`MIN(c2)` 来检索，并且可以通过从另一索引中读取一行来进行检索。即，对于每一列`c1`和 `c2`，存在其中列是索引的第一列的索引。在这种情况下，将通过读取两个确定性行来返回一行。

  `Extra`如果要读取的行不确定，则不会出现 此值。考虑以下查询：

  ```sql
  SELECT MIN(c2) FROM t1 WHERE c1 <= 10;
  ```

  假设这`(c1, c2)`是一个覆盖指数。使用此索引，`c1 <= 10`必须扫描所有具有的行以找到最小值 `c2`。相比之下，请考虑以下查询：

  ```sql
  SELECT MIN(c2) FROM t1 WHERE c1 = 10;
  ```

  在这种情况下，第一个索引行`c1 = 10`包含最小值`c2` 。仅一行必须读取才能产生返回的行。

  对于维护每个表的行数准确的存储引擎（例如`MyISAM`，但不是 `InnoDB`），对于缺少该子句或始终为true且没有 子句的查询，`Extra` 可能会出现此值。（这是一个隐式分组查询的实例，其中存储引擎影响是否可以读取确定数量的行。） `COUNT(*)``WHERE``GROUP BY`

- `Skip_open_table`， `Open_frm_only`， `Open_full_table`（JSON属性： `message`）

  这些值表示适用于`INFORMATION_SCHEMA` 表查询的文件打开优化。

  - `Skip_open_table`：不需要打开表文件。该信息已经可以从数据字典中获得。
  - `Open_frm_only`：仅数据字典需要读取表信息。
  - `Open_full_table`：未优化的信息查找。表信息必须从数据字典中读取并通过读取表文件来读取。

- `Start temporary`，`End temporary`（JSON属性： `message`）

  这表明临时表用于半联接重复淘汰策略。

- `unique row not found`（JSON属性： `message`）

  对于诸如的查询，没有行满足 索引或表中的条件。 `SELECT ... FROM *`tbl_name`*``UNIQUE``PRIMARY KEY`

- `Using filesort`（JSON属性： `using_filesort`）

  MySQL必须额外进行一遍，以找出如何按排序顺序检索行。通过根据联接类型遍历所有行并存储与该`WHERE`子句匹配的所有行的排序键和指向该行的指针来完成排序。然后对键进行排序，并按排序顺序检索行。请参见 [第8.2.1.16节“按优化排序”](https://dev.mysql.com/doc/refman/8.0/en/order-by-optimization.html)。

- `Using index`（JSON属性： `using_index`）

  仅使用索引树中的信息从表中检索列信息，而不必进行其他查找以读取实际行。当查询仅使用属于单个索引的列时，可以使用此策略。

  对于`InnoDB`具有用户定义的聚集索引的表，即使列中`Using index`不存在 该索引也可以使用`Extra`。如果`type`is [`index`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index)和 `key`is就是这种情况 `PRIMARY`。

- `Using index condition`（JSON属性： `using_index_condition`）

  通过访问索引元组并首先对其进行测试以确定是否读取完整的表行来读取表。这样，除非有必要，否则索引信息将用于延迟（“下推”）读取整个表行。请参见 [第8.2.1.6节“索引条件下推优化”](https://dev.mysql.com/doc/refman/8.0/en/index-condition-pushdown-optimization.html)。

- `Using index for group-by`（JSON属性：`using_index_for_group_by`）

  与`Using index`表访问方法类似，`Using index for group-by` 表示MySQL找到了一个索引，该索引可用于检索a`GROUP BY`或 `DISTINCT`查询的所有列，而无需对实际表进行任何额外的磁盘访问。此外，以最有效的方式使用索引，因此对于每个组，仅读取少数索引条目。有关详细信息，请参见 [第8.2.1.17节“优化组”](https://dev.mysql.com/doc/refman/8.0/en/group-by-optimization.html)。

- `Using index for skip scan`（JSON属性：`using_index_for_skip_scan`）

  表示使用跳过扫描访问方法。请参阅 [跳过扫描范围访问方法](https://dev.mysql.com/doc/refman/8.0/en/range-optimization.html#range-access-skip-scan)。

- `Using join buffer (Block Nested Loop)`， `Using join buffer (Batched Key Access)`， `Using join buffer (hash join)`（JSON属性：`using_join_buffer`）

  来自较早联接的表被部分读取到联接缓冲区中，然后从缓冲区中使用它们的行来与当前表执行联接。 `(Block Nested Loop)`表示使用块嵌套循环算法，`(Batched Key Access)`表示使用批处理密钥访问算法，并`(hash join)`表示使用哈希联接。即，[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)缓冲输出的前一行中的表中的键 ，并从出现行所在的表中批量提取匹配的行 `Using join buffer`。

  在JSON格式的输出，值 `using_join_buffer`总是之一 `Block Nested Loop`，`Batched Key Access`或`hash join`。

  从MySQL 8.0.18开始，可以使用哈希联接。MySQL 8.0.20或更高版本中不使用块嵌套循环算法。有关这些优化的更多信息，请参见[第8.2.1.4节“哈希联接优化”](https://dev.mysql.com/doc/refman/8.0/en/hash-joins.html)和“ [块嵌套循环联接算法”](https://dev.mysql.com/doc/refman/8.0/en/nested-loop-joins.html#block-nested-loop-join-algorithm)。

  有关[批量密钥](https://dev.mysql.com/doc/refman/8.0/en/bnl-bka-optimization.html#bka-optimization)访问算法的信息，请参阅[批量密钥访问联接](https://dev.mysql.com/doc/refman/8.0/en/bnl-bka-optimization.html#bka-optimization)。

- `Using MRR`（JSON属性： `message`）

  使用多范围读取优化策略读取表。请参见[第8.2.1.11节“多范围读取优化”](https://dev.mysql.com/doc/refman/8.0/en/mrr-optimization.html)。

- `Using sort_union(...)`，`Using union(...)`，`Using intersect(...)`（JSON属性： `message`）

  这些指示了特定算法，该算法显示了如何针对[`index_merge`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index_merge)联接类型合并索引扫描 。请参见[第8.2.1.3节“索引合并优化”](https://dev.mysql.com/doc/refman/8.0/en/index-merge-optimization.html)。

- `Using temporary`（JSON属性： `using_temporary_table`）

  为了解决该查询，MySQL需要创建一个临时表来保存结果。如果查询包含`GROUP BY`和 `ORDER BY`子句以不同的方式列出列，通常会发生这种情况。

- `Using where`（JSON属性： `attached_condition`）

  甲`WHERE`子句用于限制来匹配下一个表或发送到客户端的行。除非您专门打算从表中获取或检查所有行，否则如果查询中的`Extra`值不是 `Using where`且表连接类型为[`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)或 ，则 查询中可能会出错[`index`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_index)。

  `Using where`在JSON格式的输出中没有直接对应的内容；该 `attached_condition`属性包含使用的任何`WHERE`条件。

- `Using where with pushed condition`（JSON属性：`message`）

  此产品适用于[`NDB`](https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster.html) 表*只*。这意味着NDB Cluster正在使用条件下推优化来提高在非索引列和常量之间进行直接比较的效率。在这种情况下，条件被“下推”到群集的数据节点，并同时在所有数据节点上进行评估。这样就无需通过网络发送不匹配的行，并且在可以但不使用条件下推的情况下，可以将此类查询的速度提高5到10倍。有关更多信息，请参见 [第8.2.1.5节“发动机状况下推优化”](https://dev.mysql.com/doc/refman/8.0/en/engine-condition-pushdown-optimization.html)。

- `Zero limit`（JSON属性： `message`）

  该查询有一个`LIMIT 0`子句，不能选择任何行。

#### 解释输出解释

通过获取输出`rows` 列中值的乘积，可以很好地表明联接的良好程度[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。这应该大致告诉您MySQL必须检查多少行才能执行查询。如果使用[`max_join_size`](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_join_size)系统变量限制查询，则 此行乘积还用于确定[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html) 执行哪些多表语句以及中止哪个多表语句。请参见 [第5.1.1节“配置服务器”](https://dev.mysql.com/doc/refman/8.0/en/server-configuration.html)。

以下示例显示了如何根据提供的信息逐步优化多表联接 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)。

假设您在[`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)此处显示了该 语句，并计划使用进行检查 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)：

```sql
EXPLAIN SELECT tt.TicketNumber, tt.TimeIn,
               tt.ProjectReference, tt.EstimatedShipDate,
               tt.ActualShipDate, tt.ClientID,
               tt.ServiceCodes, tt.RepetitiveID,
               tt.CurrentProcess, tt.CurrentDPPerson,
               tt.RecordVolume, tt.DPPrinted, et.COUNTRY,
               et_1.COUNTRY, do.CUSTNAME
        FROM tt, et, et AS et_1, do
        WHERE tt.SubmitTime IS NULL
          AND tt.ActualPC = et.EMPLOYID
          AND tt.AssignedPC = et_1.EMPLOYID
          AND tt.ClientID = do.CUSTNMBR;
```

对于此示例，进行以下假设：

- 被比较的列已声明如下。

  | 表   | 柱           | 数据类型   |
  | :--- | :----------- | :--------- |
  | `tt` | `ActualPC`   | `CHAR(10)` |
  | `tt` | `AssignedPC` | `CHAR(10)` |
  | `tt` | `ClientID`   | `CHAR(10)` |
  | `et` | `EMPLOYID`   | `CHAR(15)` |
  | `do` | `CUSTNMBR`   | `CHAR(15)` |

- 这些表具有以下索引。

  | 表   | 指数                      |
  | :--- | :------------------------ |
  | `tt` | `ActualPC`                |
  | `tt` | `AssignedPC`              |
  | `tt` | `ClientID`                |
  | `et` | `EMPLOYID` （首要的关键） |
  | `do` | `CUSTNMBR` （首要的关键） |

- 该`tt.ActualPC`值不是均匀分布的。

最初，在执行任何优化之前，该 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)语句会产生以下信息：

```none
table type possible_keys key  key_len ref  rows  Extra
et    ALL  PRIMARY       NULL NULL    NULL 74
do    ALL  PRIMARY       NULL NULL    NULL 2135
et_1  ALL  PRIMARY       NULL NULL    NULL 74
tt    ALL  AssignedPC,   NULL NULL    NULL 3872
           ClientID,
           ActualPC
      Range checked for each record (index map: 0x23)
```

因为`type`是 [`ALL`](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html#jointype_all)针对每个表的，所以此输出表明MySQL正在生成所有表的笛卡尔积；也就是说，每行组合。这需要相当长的时间，因为必须检查每个表中的行数的乘积。对于当前情况，此乘积为74×2135×74×3872 = 45,268,558,720行。如果桌子更大，您只能想象需要多长时间。

这里的一个问题是，如果将索引声明为相同的类型和大小，MySQL可以更有效地在列上使用索引。在这种情况下，[`VARCHAR`](https://dev.mysql.com/doc/refman/8.0/en/char.html)与 [`CHAR`](https://dev.mysql.com/doc/refman/8.0/en/char.html)被认为是相同的，如果它们被声明为相同的大小。 `tt.ActualPC`被声明为 `CHAR(10)`和`et.EMPLOYID` 是`CHAR(15)`，因此存在长度不匹配。

若要解决此列长度之间的差异，请使用 从10个字符[`ALTER TABLE`](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)延长 `ActualPC`到15个字符：

```sql
mysql> ALTER TABLE tt MODIFY ActualPC VARCHAR(15);
```

现在`tt.ActualPC`和 `et.EMPLOYID`都是 `VARCHAR(15)`。[`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)再次执行该 语句将产生以下结果：

```none
table type   possible_keys key     key_len ref         rows    Extra
tt    ALL    AssignedPC,   NULL    NULL    NULL        3872    Using
             ClientID,                                         where
             ActualPC
do    ALL    PRIMARY       NULL    NULL    NULL        2135
      Range checked for each record (index map: 0x1)
et_1  ALL    PRIMARY       NULL    NULL    NULL        74
      Range checked for each record (index map: 0x1)
et    eq_ref PRIMARY       PRIMARY 15      tt.ActualPC 1
```

这不是完美的，但是更好：`rows`值的乘积 少了74倍。此版本在几秒钟内执行。

可以进行第二种更改以消除`tt.AssignedPC = et_1.EMPLOYID`和`tt.ClientID = do.CUSTNMBR`比较的列长不匹配：

```sql
mysql> ALTER TABLE tt MODIFY AssignedPC VARCHAR(15),
                      MODIFY ClientID   VARCHAR(15);
```

修改之后， [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)产生如下所示的输出：

```none
table type   possible_keys key      key_len ref           rows Extra
et    ALL    PRIMARY       NULL     NULL    NULL          74
tt    ref    AssignedPC,   ActualPC 15      et.EMPLOYID   52   Using
             ClientID,                                         where
             ActualPC
et_1  eq_ref PRIMARY       PRIMARY  15      tt.AssignedPC 1
do    eq_ref PRIMARY       PRIMARY  15      tt.ClientID   1
```

在这一点上，查询尽可能地被优化。剩下的问题是，默认情况下，MySQL假定该`tt.ActualPC` 列中的值是均匀分布的，而`tt`表不是这种情况。幸运的是，很容易告诉MySQL分析密钥分布：

```sql
mysql> ANALYZE TABLE tt;
```

使用其他索引信息，联接是完美的，并 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)产生以下结果：

```none
table type   possible_keys key     key_len ref           rows Extra
tt    ALL    AssignedPC    NULL    NULL    NULL          3872 Using
             ClientID,                                        where
             ActualPC
et    eq_ref PRIMARY       PRIMARY 15      tt.ActualPC   1
et_1  eq_ref PRIMARY       PRIMARY 15      tt.AssignedPC 1
do    eq_ref PRIMARY       PRIMARY 15      tt.ClientID   1
```

在`rows`从输出列 [`EXPLAIN`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)是一个受过教育的猜测从MySQL联接优化。通过将`rows`乘积与查询返回的实际行数进行比较，检查数字是否接近真实 值。如果数字完全不同，则可以通过`STRAIGHT_JOIN`在 [`SELECT`](https://dev.mysql.com/doc/refman/8.0/en/select.html)语句中使用并尝试在`FROM`子句中以不同顺序列出表来 获得更好的性能 。（但是，`STRAIGHT_JOIN`由于禁用了半[联接转换](https://dev.mysql.com/doc/refman/8.0/en/semijoins.html)， 可能会阻止使用索引。请参见[第8.2.2.1节“](https://dev.mysql.com/doc/refman/8.0/en/semijoins.html)使用半 [联接转换优化IN和EXISTS子查询谓词”）](https://dev.mysql.com/doc/refman/8.0/en/semijoins.html)）

在某些情况下，可能会执行[`EXPLAIN SELECT`](https://dev.mysql.com/doc/refman/8.0/en/explain.html)与子查询一起使用时会修改数据的语句。有关更多信息，请参见[第13.2.11.8节“派生表”](https://dev.mysql.com/doc/refman/8.0/en/derived-tables.html)。