import { Link } from "react-router-dom";
function Hero() {
  return (
    <section className="hero">
      <h1>🎓 Student Portal</h1>

      <p>
        Learn React through a modern, responsive Student Portal.
      </p>

      <Link to="/courses">
    <button>Explore Courses</button>
</Link>
    </section>
  );
}

export default Hero;