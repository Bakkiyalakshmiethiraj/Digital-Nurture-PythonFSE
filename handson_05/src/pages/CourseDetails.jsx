import { useParams, useNavigate } from "react-router-dom";
import courses from "../data/courses";
import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function CourseDetails() {
  const { id } = useParams();
  const navigate = useNavigate();

  const course = courses.find((c) => c.id === Number(id));

  const {
  enrolledCourses,
  enrollCourse,
  withdrawCourse,
} = useContext(EnrollmentContext);

const enrolled = enrolledCourses.some(
  (c) => c.id === course.id
);

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  return (
    <section className="page">

      <h1>{course.name}</h1>

      <p>
        <strong>Instructor:</strong> {course.instructor}
      </p>

      <p>
        <strong>Credits:</strong> {course.credits}
      </p>

      <p>
        <strong>Description:</strong> {course.description}
      </p>
      
      <button
  onClick={() => {
    if (enrolled) {
      withdrawCourse(course.id);
    } else {
      enrollCourse(course);
    }
  }}
  className={enrolled ? "withdraw-btn" : "enroll-btn"}
>
  {enrolled ? "Withdraw" : "Enroll"}
</button>

{enrolled && (
  <p className="success-message">
    ✅ You are successfully enrolled in this course.
  </p>
)}
      
      <button
  className="back-btn"
  onClick={() => navigate("/courses")}
>
  ← Back to Courses
</button>

    </section>
  );
}

export default CourseDetails;