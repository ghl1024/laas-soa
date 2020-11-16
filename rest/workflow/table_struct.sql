create table workflow_struct
(
    id              int auto_increment comment '自增主键, 同时作为版本号'
        primary key,
    service_type    varchar(100)                        not null comment '业务类型',
    workflow        varchar(255)                        not null comment '流程中的角色的审核顺序',
    create_by       varchar(100)                        not null comment '创建人',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '流程模板';

create table workflow_data
(
    id              int auto_increment comment '自增主键'
        primary key,
    title           varchar(255)                        not null comment '标题',
    service_type    varchar(255)                        not null comment '业务类型',
    form_data_id    int                                 not null comment '表单数据id',
    form_data       mediumtext                          not null comment '表单数据',
    steps           varchar(255)                        not null comment '整体审核人流程',
    next_steps      varchar(255)                        not null comment '剩余审核人流程',
    next_step       varchar(100)                        not null comment '下一个审核人',
    group_id        int                                 null comment '流程组的id',
    execute_order   int                                 null comment '执行顺序',
    status          varchar(100)                        not null comment '流程状态',
    service_status  varchar(100)                        not null comment '业务执行状态',
    create_by       varchar(100)                        not null comment '创建人',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '流程实例';

create table workflow_data_record
(
    id              int auto_increment comment '自增主键'
        primary key,
    workflow_id     int                                 not null comment '流程id',
    status          varchar(100)                        not null comment '状态',
    create_by       varchar(100)                        not null comment '创建人',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '流程实例记录';

create table workflow_business_log
(
    id              int auto_increment comment '自增主键'
        primary key,
    workflow_id     int                                 not null comment '流程id',
    content         mediumtext                          not null comment '内容',
    create_by       varchar(100)                        not null comment '创建人',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '流程日志';

create table workflow_business_rollback
(
    id              int auto_increment
        primary key,
    workflow_id     int                                 not null comment '流程id',
    content         mediumtext                          not null comment '内容',
    create_datetime timestamp default CURRENT_TIMESTAMP not null comment '创建时间'
)
    comment '流程业务回滚';






