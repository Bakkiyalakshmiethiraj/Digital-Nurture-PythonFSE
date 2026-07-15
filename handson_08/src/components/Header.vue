<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const enrollmentStore = useEnrollmentStore();
</script>

<template>
  <div class="header-wrapper">
    <header class="app-header">
      <div class="brand">
        <div class="logo-icon">SMP</div>
        <h2>Student Management Portal</h2>
      </div>
      <nav class="navigation">
        <RouterLink to="/" class="nav-link">Home</RouterLink>
        <RouterLink to="/courses" class="nav-link">Courses</RouterLink>
        <RouterLink to="/profile" class="nav-link">Profile</RouterLink>
        <RouterLink to="/announcements" class="nav-link">Announcements</RouterLink>
      </nav>
      <div class="status-badge">
        Enrolled Count: <span class="badge-count">{{ enrollmentStore.enrolledCourses.length }}</span>
      </div>
    </header>

    <!-- Global Dynamic Toast Notification System -->
    <transition name="slide-down">
      <div v-if="enrollmentStore.notification" :class="['toast-banner', enrollmentStore.notification.type]">
        {{ enrollmentStore.notification.message }}
      </div>
    </transition>
  </div>
</template>

<style scoped>
.header-wrapper {
  position: relative;
  z-index: 100;
}
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
  height: 70px;
  background-color: #0f172a;
  color: white;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon {
  background: var(--primary-color);
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.brand h2 {
  font-size: 1.15rem;
  margin: 0;
  letter-spacing: 0.5px;
}

.navigation {
  display: flex;
  gap: 8px;
}

.nav-link {
  color: #94a3b8;
  text-decoration: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 500;
  transition: all 0.2s;
}

.nav-link:hover {
  color: white;
  background: rgba(255, 255, 255, 0.05);
}

.nav-link.router-link-active {
  color: white;
  background: var(--primary-color);
}

.status-badge {
  font-size: 0.9rem;
  background: rgba(255, 255, 255, 0.08);
  padding: 6px 14px;
  border-radius: 20px;
}

.badge-count {
  color: var(--success-color);
  font-weight: bold;
}

/* Toast styling */
.toast-banner {
  position: fixed;
  top: 85px;
  right: 20px;
  padding: 12px 24px;
  border-radius: 8px;
  color: white;
  font-weight: 500;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}
.success { background-color: var(--success-color); }
.warning { background-color: #f59e0b; }
.danger { background-color: var(--danger-color); }

.slide-down-enter-from, .slide-down-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>