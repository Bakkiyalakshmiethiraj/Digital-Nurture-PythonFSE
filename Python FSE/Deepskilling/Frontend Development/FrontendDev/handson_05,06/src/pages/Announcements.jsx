import { useEffect, useState } from "react";
import { getPosts } from "../services/api";
import Loading from "../components/Loading";

function Announcements() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadData() {
      try {
        const data = await getPosts();
        setPosts(data);
      } catch (err) {
        setError("Failed to load announcements.");
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);

  return (
    <section className="page">
      <h1>📢 Announcements</h1>

     
      {loading && <Loading />}

      {error && <p style={{ color: "red" }}>{error}</p>}

      <div className="announcement-grid">
        {posts.map((post) => (
          <div key={post.id} className="announcement-card">
            <h3>{post.title}</h3>
            <p>{post.body}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Announcements;