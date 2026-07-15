import CourseCard from "./CourseCard";

function CourseList({ courses }) {

    if(courses.length===0){

        return(

            <h2 style={{textAlign:"center"}}>
                No Courses Found
            </h2>

        );

    }

    return(

        <div className="course-grid">

            {courses.map(course=>

                <CourseCard
                    key={course.id}
                    course={course}
                />

            )}

        </div>

    );

}

export default CourseList;