<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

const route = useRoute();
const router = useRouter();
const enrollmentStore = useEnrollmentStore();

const courseId = route.params.id;
const course = ref(null);

onMounted(() => {
  // Mocking database fetch based on courseId
  const mockCourses = [
    { id: '1', name: 'Introduction to Vue.js', code: 'CS101', credits: 3, description: 'Learn the fundamentals of Vue 3.' },
    { id: '2', name: 'Advanced State Management with Pinia', code: 'CS102', credits: 4, description: 'Master global state in Vue apps.' },
    { id: '3', name: 'Web Application Routing', code: 'CS103', credits: 3, description: 'Deep dive into single-page application routing.' },
    { id: '4', name: 'Frontend Architecture', code: 'CS104', credits: 4, description: 'Scale large applications cleanly.' },
    { id: '5', name: 'UI/UX Design Fundamentals', code: 'CS105', credits: 2, description: 'Design user-friendly web interfaces.' }
  ];
  
  course.value = mockCourses.find(c => c.id === courseId);
});

const handleEnroll = () => {
  if (course.value) {
    enrollmentStore.enroll(course.value);
    router.push('/profile');
  }
};
</script>

<template>
  <div v-if="course" class="detail-container">
    <h2>{{ course.name }} Details</h2>
    <p><strong>Code:</strong> {{ course.code }}</p>
    <p><strong>Credits:</strong> {{ course.credits }}</p>
    <p><strong>Description:</strong> {{ course.description }}</p>
    <button @click="handleEnroll" class="enroll-btn">Enroll in Course</button>
  </div>
  <div v-else>
    <p>Loading course details...</p>
  </div>
</template>

<style scoped>
.detail-container {
  padding: 20px;
  border: 1px solid #ddd;
}
.enroll-btn {
  padding: 10px 20px;
  background-color: #42b883;
  color: white;
  border: none;
  cursor: pointer;
}
</style>