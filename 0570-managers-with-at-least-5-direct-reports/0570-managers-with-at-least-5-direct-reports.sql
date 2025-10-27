# Write your MySQL query statement below
select e.name 
from Employee e 
join(
    select managerId ,count(managerId) as man 
    from Employee 
    group by managerId
)m
on e.id = m.managerId
where m.man >= 5