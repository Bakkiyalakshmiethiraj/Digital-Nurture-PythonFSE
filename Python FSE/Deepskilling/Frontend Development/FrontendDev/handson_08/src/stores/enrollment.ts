import { ref, computed } from 'vue';
import { defineStore } from 'pinia';

export const useEnrollmentStore = defineStore('enrollment', () => {
  // State initialization with localStorage persistence
  const enrolledCourses = ref(JSON.parse(localStorage.getItem('enrolled_courses')) || []);
  const notification = ref(null);

  // Computed properties
  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0);
  });

  // Helper function to show notifications
  function showToast(message, type = 'success') {
    notification.value = { message, type };
    setTimeout(() => {
      notification.value = null;
    }, 3500);
  }

  // Actions
  function enroll(course) {
    const alreadyEnrolled = enrolledCourses.value.some(c => c.id === course.id);
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course);
      localStorage.setItem('enrolled_courses', JSON.stringify(enrolledCourses.value));
      showToast(`Successfully enrolled in ${course.name}!`, 'success');
    } else {
      showToast(`You are already enrolled in ${course.name}.`, 'warning');
    }
  }

  function unenroll(courseId) {
    const course = enrolledCourses.value.find(c => c.id === courseId);
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId);
    localStorage.setItem('enrolled_courses', JSON.stringify(enrolledCourses.value));
    if (course) {
      showToast(`Dropped ${course.name} from your profile.`, 'danger');
    }
  }

  return { enrolledCourses, totalCredits, notification, enroll, unenroll };
});