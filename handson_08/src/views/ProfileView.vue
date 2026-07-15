<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const enrollmentStore = useEnrollmentStore();
</script>

<template>
  <div class="profile-layout">
    <div class="profile-main">
      <h2>Enrolled Syllabus Overview</h2>
      
      <!-- Empty State handling -->
      <div v-if="enrollmentStore.enrolledCourses.length === 0" class="empty-state">
        <div class="empty-icon">📂</div>
        <h3>No Courses Active</h3>
        <p>Your academic schedule is currently empty. Head over to the course catalog to add items.</p>
        <RouterLink to="/courses" class="browse-link">Browse Catalog</RouterLink>
      </div>
      
      <div v-else class="list-container">
        <div v-for="course in enrollmentStore.enrolledCourses" :key="course.id" class="enrolled-row">
          <div>
            <h4>{{ course.name }}</h4>
            <p>{{ course.code }} • {{ course.credits }} Academic Credits</p>
          </div>
          <button @click="enrollmentStore.unenroll(course.id)" class="drop-btn">Drop Course</button>
        </div>
      </div>
    </div>

    <!-- Summary Sidebar Panel -->
    <div class="summary-sidebar">
      <h3>Registration Metrics</h3>
      <div class="metric-card">
        <span class="metric-label">Total Selected Modules</span>
        <span class="metric-value">{{ enrollmentStore.enrolledCourses.length }}</span>
      </div>
      <div class="metric-card">
        <span class="metric-label">Aggregated Credits</span>
        <span class="metric-value credit-total">{{ enrollmentStore.totalCredits }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 32px;
}
@media (max-width: 768px) {
  .profile-layout { grid-template-columns: 1fr; }
}

.profile-main, .summary-sidebar {
  background: var(--card-bg);
  padding: 30px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.empty-state {
  text-align: center;
  padding: 40px 20px;
}
.empty-icon { font-size: 3rem; margin-bottom: 12px; }
.browse-link {
  display: inline-block;
  margin-top: 15px;
  background: var(--primary-color);
  color: white;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 500;
}

.enrolled-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid var(--border-color);
}
.enrolled-row h4 { margin: 0 0 4px 0; font-size: 1.05rem; }
.enrolled-row p { margin: 0; color: var(--text-muted); font-size: 0.875rem; }

.drop-btn {
  background: #fef2f2;
  color: var(--danger-color);
  border: 1px solid #fee2e2;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.2s;
}
.drop-btn:hover { background: var(--danger-color); color: white; }

.metric-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8fafc;
  padding: 16px;
  border-radius: 8px;
  margin-top: 12px;
}
.metric-label { font-size: 0.9rem; color: var(--text-muted); }
.metric-value { font-weight: 700; font-size: 1.2rem; }
.credit-total { color: var(--primary-color); }
</style>