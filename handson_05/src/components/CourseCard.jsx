import { Link } from "react-router-dom";

function CourseCard({ course }) {
  return (
    <div className="course-card">
      <h3>{course.name}</h3>

      <p>
        <strong>Instructor:</strong> {course.instructor}
      </p>

      <p>
        <strong>Credits:</strong> {course.credits}
      </p>

      <Link to={`/courses/${course.id}`}>
        <button>View Details</button>
      </Link>
    </div>
  );
}

export default CourseCard;