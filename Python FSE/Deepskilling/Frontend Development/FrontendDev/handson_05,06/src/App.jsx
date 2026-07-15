import Header from "./components/Header";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Courses from "./pages/Courses";
import Students from "./pages/Students";
import Profile from "./pages/Profile";
import Contact from "./pages/Contact";
import NotFound from "./pages/NotFound";
import Announcements from "./pages/Announcements";
import CourseDetails from "./pages/CourseDetails";

import { Routes, Route } from "react-router-dom";

import "./App.css";

function App() {
  return (
    <div className="app">

      <Header />

      <main className="main-content">

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/students" element={<Students />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/announcements" element={<Announcements />} />
          <Route path="/courses/:id" element={<CourseDetails />} />
        </Routes>

      </main>

      <Footer />

    </div>
  );
}

export default App;