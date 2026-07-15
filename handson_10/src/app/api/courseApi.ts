import apiClient from './apiClient';

export const getAllCourses = async () => {
  return await apiClient.get('/users');
};

export const getCourseById = async (id: number) => {
  return await apiClient.get(`/users/${id}`);
};

export const enrollStudent = async (
  studentId: number,
  courseId: number
) => {
  return await apiClient.post('/posts', {
    studentId,
    courseId
  });
};