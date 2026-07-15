## SQL PROGRAM:

```
select table_name
from information_schema.tables
where table_schema = 'public';

alter table students
add column phone_number varchar(15);

alter table courses
add column max_seats int;

alter table courses
add constraint chk_max_seats
check (max_seats > 0);

alter table departments
rename column hod_name to head_of_department;

alter table students
drop column phone_number;

select column_name
from information_schema.columns
where table_name = 'departments';

select column_name
from information_schema.columns
where table_name = 'courses';


select column_name
from information_schema.columns
where table_name = 'students';

insert into departments (dept_name, head_of_department, budget)
values
('computer science', 'dr. ravi kumar', 1200000.00),
('electronics', 'dr. priya sharma', 1000000.00),
('mechanical', 'dr. arun kumar', 900000.00);
select * from departments;

insert into students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
values
('rahul', 'sharma', 'rahul@gmail.com', '2004-05-10', 1, 2022),
('anita', 'singh', 'anita@gmail.com', '2003-08-20', 2, 2022),
('vijay', 'kumar', 'vijay@gmail.com', '2004-01-15', 3, 2023),
('meena', 'patel', 'meena@gmail.com', '2003-11-30', 1, 2022),
('akash', 'verma', 'akash@gmail.com', '2004-02-25', 2, 2023);
select * from students;

insert into courses
(course_name, course_code, credits, department_id, max_seats)
values
('database management systems', 'cs301', 4, 1, 60),
('digital electronics', 'ec201', 3, 2, 50),
('thermodynamics', 'me301', 4, 3, 45),
('operating systems', 'cs302', 4, 1, 60);
select * from courses;

insert into professors
(prof_name, email, department_id, salary)
values
('dr. ravi', 'ravi@college.edu', 1, 95000),
('dr. priya', 'priya@college.edu', 2, 90000),
('dr. arun', 'arun@college.edu', 3, 85000);
select * from professors;

insert into enrollments
(student_id, course_id, enrollment_date, grade)
values
(1, 1, '2022-07-15', 'a'),
(2, 2, '2022-07-16', 'b'),
(3, 3, '2023-07-17', 'a'),
(4, 4, '2022-07-18', 'c'),
(5, 2, '2023-07-19', null);
select * from enrollments;

update enrollments
set grade = 'b'
where student_id = 4;

delete from enrollments
where grade is null;

select * from students;
select *
from students
where enrollment_year = 2022;

select *
from courses
where credits > 3;

select *
from professors
where salary between 85000 and 95000;

select *
from students
where email like '%gmail%';

select *
from students
order by first_name;

select *
from professors
order by salary desc;

select count(*) as total_students
from students;

select avg(salary) as average_salary
from professors;

select max(salary) as highest_salary
from professors;

select min(salary) as lowest_salary
from professors;

select department_id,
count(*) as total_students
from students
group by department_id;

select department_id,
avg(salary) as average_salary
from professors
group by department_id;

select department_id,
count(*) as total_students
from students
group by department_id
having count(*) > 1;


select table_name
from information_schema.tables
where table_schema = 'public';

alter table students
add column phone_number varchar(15);

alter table courses
add column max_seats int;

alter table courses
add constraint chk_max_seats
check (max_seats > 0);

alter table departments
rename column hod_name to head_of_department;

alter table students
drop column phone_number;

select column_name
from information_schema.columns
where table_name = 'departments';

select column_name
from information_schema.columns
where table_name = 'courses';


select column_name
from information_schema.columns
where table_name = 'students';

insert into departments (dept_name, head_of_department, budget)
values
('computer science', 'dr. ravi kumar', 1200000.00),
('electronics', 'dr. priya sharma', 1000000.00),
('mechanical', 'dr. arun kumar', 900000.00);
select * from departments;

insert into students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
values
('rahul', 'sharma', 'rahul@gmail.com', '2004-05-10', 1, 2022),
('anita', 'singh', 'anita@gmail.com', '2003-08-20', 2, 2022),
('vijay', 'kumar', 'vijay@gmail.com', '2004-01-15', 3, 2023),
('meena', 'patel', 'meena@gmail.com', '2003-11-30', 1, 2022),
('akash', 'verma', 'akash@gmail.com', '2004-02-25', 2, 2023);
select * from students;

insert into courses
(course_name, course_code, credits, department_id, max_seats)
values
('database management systems', 'cs301', 4, 1, 60),
('digital electronics', 'ec201', 3, 2, 50),
('thermodynamics', 'me301', 4, 3, 45),
('operating systems', 'cs302', 4, 1, 60);
select * from courses;

insert into professors
(prof_name, email, department_id, salary)
values
('dr. ravi', 'ravi@college.edu', 1, 95000),
('dr. priya', 'priya@college.edu', 2, 90000),
('dr. arun', 'arun@college.edu', 3, 85000);
select * from professors;

insert into enrollments
(student_id, course_id, enrollment_date, grade)
values
(1, 1, '2022-07-15', 'a'),
(2, 2, '2022-07-16', 'b'),
(3, 3, '2023-07-17', 'a'),
(4, 4, '2022-07-18', 'c'),
(5, 2, '2023-07-19', null);
select * from enrollments;

update enrollments
set grade = 'b'
where student_id = 4;

delete from enrollments
where grade is null;

select * from students;
select *
from students
where enrollment_year = 2022;

select *
from courses
where credits > 3;

select *
from professors
where salary between 85000 and 95000;

select *
from students
where email like '%gmail%';

select *
from students
order by first_name;

select *
from professors
order by salary desc;

select count(*) as total_students
from students;

select avg(salary) as average_salary
from professors;

select max(salary) as highest_salary
from professors;

select min(salary) as lowest_salary
from professors;

select department_id,
count(*) as total_students
from students
group by department_id;

select department_id,
avg(salary) as average_salary
from professors
group by department_id;

select department_id,
count(*) as total_students
from students
group by department_id
having count(*) > 1;


select s.student_id,
       s.first_name,
       s.last_name,
       d.dept_name
from students s
inner join departments d
on s.department_id = d.department_id;

select s.first_name,
       c.course_name,
       e.grade
from students s
inner join enrollments e
on s.student_id = e.student_id
inner join courses c
on e.course_id = c.course_id;

select s.first_name,
       c.course_name
from students s
left join enrollments e
on s.student_id = e.student_id
left join courses c
on e.course_id = c.course_id;

select c.course_name,
       count(e.student_id) as total_students
from courses c
left join enrollments e
on c.course_id = e.course_id
group by c.course_name;

select p.prof_name,
       d.dept_name,
       p.salary
from professors p
inner join departments d
on p.department_id = d.department_id;
```
## SQL OUTPUT:

<img width="1263" height="653" alt="image" src="https://github.com/user-attachments/assets/f2b38f90-9d67-4f25-81a4-a87616164629" />
<img width="1267" height="652" alt="image" src="https://github.com/user-attachments/assets/bddd6e56-e66a-42d9-96ab-98d380712326" />
<img width="1262" height="653" alt="image" src="https://github.com/user-attachments/assets/68904dc0-7191-4115-84a0-f9c1a07d6f1f" />
<img width="1262" height="657" alt="image" src="https://github.com/user-attachments/assets/378b648e-ae9f-485a-8be2-e61396b5dfb8" />
<img width="1268" height="648" alt="image" src="https://github.com/user-attachments/assets/eeb59562-173c-412e-a359-4699591a9b6c" />





