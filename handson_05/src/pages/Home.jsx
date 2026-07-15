import Hero from "../components/Hero";

function Home() {
  return (
    <>
      <Hero />

      <section className="page">
        <h2>Welcome to the Student Portal</h2>

        <p>
          This portal helps students explore available courses, view announcements,
          and manage their academic profile.
        </p>

        <div className="home-features">

          <div className="feature-card">
            <h3>📚 Courses</h3>
            <p>Browse all available courses.</p>
          </div>

          <div className="feature-card">
            <h3>📢 Announcements</h3>
            <p>Stay updated with the latest news.</p>
          </div>

          <div className="feature-card">
            <h3>👤 Profile</h3>
            <p>Manage your student information.</p>
          </div>

        </div>

      </section>
    </>
  );
}

export default Home;