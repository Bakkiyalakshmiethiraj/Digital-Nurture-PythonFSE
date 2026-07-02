## SQL PROGRAM:
```
select first_name,
       last_name
from students
where department_id = (
    select department_id
    from departments
    where dept_name = 'computer science'
);

select first_name,
       last_name
from students
where department_id = (
    select department_id
    from departments
    where dept_name = 'computer science'
);

select *
from professors
where salary = (
    select max(salary)
    from professors
);

select *
from courses
where credits >
(
    select avg(credits)
    from courses
);

select first_name,
       last_name
from students
where student_id in
(
    select student_id
    from enrollments
    where grade = 'a'
);

create view student_department_view as
select s.student_id,
       s.first_name,
       s.last_name,
       d.dept_name
from students s
join departments d
on s.department_id = d.department_id;

select *
from student_department_view;

create view professor_department_view as
select p.prof_name,
       d.dept_name,
       p.salary
from professors p
join departments d
on p.department_id = d.department_id;

select *
from professor_department_view;

drop view student_department_view;

drop view professor_department_view;

create or replace function get_total_students()
returns integer
language sql
as $$
    select count(*) from students;
$$;

select get_total_students();

create or replace function get_average_salary()
returns numeric
language sql
as $$
    select avg(salary) from professors;
$$;

select get_average_salary();
begin;

update professors
set salary = 100000
where professor_id = 1;

select * from professors;
rollback;
begin;

update professors
set salary = 98000
where professor_id = 1;

commit;
begin;

update professors
set salary = 99000
where professor_id = 2;

savepoint sp1;

update professors
set salary = 105000
where professor_id = 3;

rollback to sp1;

commit;
```
## SQL OUTPUT:
<img width="1267" height="567" alt="image" src="https://github.com/user-attachments/assets/44d273aa-11b3-4f5d-b318-8fcc16e3aca5" />
<img width="1267" height="656" alt="image" src="https://github.com/user-attachments/assets/8e52fdc8-43de-4d95-9e5b-79f047b5ac4c" />
<img width="1266" height="655" alt="image" src="https://github.com/user-attachments/assets/b047b6d3-8a42-44b9-8850-1f24e4420b38" />
<img width="1267" height="650" alt="image" src="https://github.com/user-attachments/assets/a907fa7c-075b-4e1b-8436-708a5e970072" />



