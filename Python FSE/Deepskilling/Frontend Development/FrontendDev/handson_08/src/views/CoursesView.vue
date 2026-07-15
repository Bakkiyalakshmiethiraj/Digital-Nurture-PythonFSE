<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';
import CourseCard from '../components/CourseCard.vue';

const router = useRouter();
const enrollmentStore = useEnrollmentStore();

const courses = ref([]);
const searchTerm = ref('');

onMounted(() => {
  courses.value = [
    { id: '1', name: 'Introduction to Vue.js', code: 'CS101', credits: 3 },
    { id: '2', name: 'Advanced State Management with Pinia', code: 'CS102', credits: 4 },
    { id: '3', name: 'Web Application Routing', code: 'CS103', credits: 3 },
    { id: '4', name: 'Frontend Architecture & Optimization', code: 'CS104', credits: 4 },
    { id: '5', name: 'UI/UX Design Fundamentals', code: 'CS105', credits: 2 }
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>

<template>
  <div>
    <div class="view-header">
      <div>
        <h1>Explore Academic Programs</h1>
        <p class="subtitle">Select and enroll in premium industrial technology frameworks.</p>
      </div>
      <input 
        v-model="searchTerm" 
        type="text" 
        placeholder="🔍 Search via course title or module code..." 
        class="search-bar"
      />
    </div>

    <div class="courses-grid">
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
      >
        <button class="btn-secondary" @click="router.push(`/courses/${course.id}`)">Details</button>
        <button class="btn-primary" @click="enrollmentStore.enroll(course)">Quick Enroll</button>
      </CourseCard>
    </div>
  </div>
</template>

<style scoped>
.view-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 20px;
}
h1 { font-size: 2rem; margin: 0; color: var(--text-main); }
.subtitle { color: var(--text-muted); margin: 4px 0 0 0; }

.search-bar {
  padding: 12px 20px;
  width: 100%;
  max-width: 360px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 0.95rem;
  outline: none;
  transition: border-color 0.2s;
}
.search-bar:focus { border-color: var(--primary-color); }

.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

button {
  flex: 1;
  padding: 10px 14px;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  border: none;
  transition: background 0.2s;
}
.btn-primary { background: var(--primary-color); color: white; }
.btn-primary:hover { background: var(--primary-hover); }
.btn-secondary { background: #f1f5f9; color: var(--text-main); }
.btn-secondary:hover { background: #e2e8f0; }
</style>