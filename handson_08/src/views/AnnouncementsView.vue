<script setup>
import { ref } from 'vue';

const announcements = ref([
  {
    id: 1,
    title: "Cognizant Placement Drive Registration Open",
    date: "July 15, 2026",
    content: "Eligible students must register on the portal before the end of the week. Ensure your profile metrics are up to date.",
    tag: "Urgent",
    tagClass: "tag-urgent"
  },
  {
    id: 2,
    title: "End Semester Project Submission Deadline",
    date: "July 20, 2026",
    content: "All Vue.js Hands-on exercises must be pushed to your GitHub repository by 11:59 PM.",
    tag: "Academic",
    tagClass: "tag-academic"
  },
  {
    id: 3,
    title: "Guest Lecture: Frontend Architecture Trends",
    date: "July 25, 2026",
    content: "Join us for an interactive session with industry experts discussing Vue 3, React, and Next-gen state management.",
    tag: "Event",
    tagClass: "tag-event"
  }
]);
</script>

<template>
  <div class="announcements-container">
    <div class="view-header">
      <h1>Campus Announcements</h1>
      <p class="subtitle">Stay updated with the latest notices and placement news.</p>
    </div>

    <div class="announcements-list">
      <div v-for="notice in announcements" :key="notice.id" class="notice-card">
        <div class="notice-header">
          <span :class="['notice-tag', notice.tagClass]">{{ notice.tag }}</span>
          <span class="notice-date">{{ notice.date }}</span>
        </div>
        <h3 class="notice-title">{{ notice.title }}</h3>
        <p class="notice-content">{{ notice.content }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.view-header {
  margin-bottom: 30px;
}
h1 { font-size: 2rem; margin: 0; color: var(--text-main); }
.subtitle { color: var(--text-muted); margin-top: 4px; }

.announcements-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.notice-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.notice-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.notice-tag {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 20px;
  text-transform: uppercase;
}

.tag-urgent { background: #fee2e2; color: #ef4444; }
.tag-academic { background: #e0f2fe; color: #0284c7; }
.tag-event { background: #dcfce7; color: #16a34a; }

.notice-date {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.notice-title {
  margin: 0 0 10px 0;
  font-size: 1.25rem;
  color: var(--text-main);
}

.notice-content {
  margin: 0;
  color: #475569;
  line-height: 1.6;
}
</style>