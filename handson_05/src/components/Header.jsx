import { NavLink } from "react-router-dom";
import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function Header() {
  const { enrolledCourses } = useContext(EnrollmentContext);
  return (
    <header>
      <h2>
    🎓 Student Portal
    <span className="enrolled-count">
      Enrolled: {enrolledCourses.length}
    </span>
  </h2>
      <nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/courses">Courses</NavLink>
        <NavLink to="/students">Students</NavLink>
        <NavLink to="/profile">Profile</NavLink>
        <NavLink to="/contact">Contact</NavLink>
        <NavLink to="/announcements">Announcements</NavLink>
      </nav>
    </header>
  );
}

export default Header;