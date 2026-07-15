import { useContext, useState } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function Profile() {
  const { enrolledCourses } = useContext(EnrollmentContext);

  const [name, setName] = useState("John Doe");
  const [email, setEmail] = useState("john@example.com");
  const [semester, setSemester] = useState("Semester 5");

  return (
    <section className="page">
      <h1>Student Profile</h1>

      <div className="profile-form">
        <label>Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <label>Semester</label>
        <input
          type="text"
          value={semester}
          onChange={(e) => setSemester(e.target.value)}
        />
      </div>

      <h2>My Enrolled Courses</h2>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled yet.</p>
      ) : (
        <ul>
          {enrolledCourses.map((course) => (
            <li key={course.id}>
              <strong>{course.name}</strong> — {course.instructor}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}

export default Profile;