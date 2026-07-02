## SQL PROGRAM:
```
select s.first_name,
       c.course_name
from students s
join enrollments e
on s.student_id = e.student_id
join courses c
on e.course_id = c.course_id;

create index idx_students_department
on students(department_id);

create index idx_courses_code
on courses(course_code);

create index idx_enrollments_student
on enrollments(student_id);

select indexname,
       tablename
from pg_indexes
where schemaname = 'public';

explain
select s.first_name,
       c.course_name
from students s
join enrollments e
on s.student_id = e.student_id
join courses c
on e.course_id = c.course_id;
```
## SQL OUTPUT:
<img width="1267" height="652" alt="image" src="https://github.com/user-attachments/assets/b96f6366-c7a2-43ae-bd6e-3190fdb4967f" />
<img width="1265" height="650" alt="image" src="https://github.com/user-attachments/assets/faffafa7-a71b-490d-8779-f7e8fe9b1edb" />
<img width="1257" height="657" alt="image" src="https://github.com/user-attachments/assets/bb441a28-7cba-4382-83e0-9e7a61f957e7" />


