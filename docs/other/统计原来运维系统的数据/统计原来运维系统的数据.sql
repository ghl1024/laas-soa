-- 最近一个月协作了470次
select count(1)
from deploy_orders
where created_at > date_add(now(), interval -1 month)

-- 最近一个月上线了470次
select count(1)
from deploy_orders
where created_at > date_add(now(), interval -1 month)
  and status > 2

-- 最近一个月每天上线次数
select DATE_FORMAT(created_at, '%Y-%m-%d') day, count(1)
from deploy_orders
where created_at > date_add(now(), interval -1 month)
GROUP BY day