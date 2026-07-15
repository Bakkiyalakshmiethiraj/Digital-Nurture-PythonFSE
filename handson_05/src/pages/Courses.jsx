import { useState } from "react";
import SearchBar from "../components/SearchBar";
import CourseList from "../components/CourseList";
import courses from "../data/courses";

function Courses() {
  const [search, setSearch] = useState("");

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <section className="page">
      <h1>Available Courses</h1>

      <SearchBar
        search={search}
        setSearch={setSearch}
      />

      <CourseList courses={filteredCourses} />
    </section>
  );
}

export default Courses;