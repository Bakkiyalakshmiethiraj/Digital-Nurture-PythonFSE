import { Injectable } from '@angular/core';
import { Observable, from } from 'rxjs';
import { Course } from '../models/course';
import { getAllCourses } from '../api/courseApi';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor() {}

  // ===== Hands-On 7 (Local Data) =====

  private courses: Course[] = [
    {
      id: 1,
      name: 'HTML & CSS',
      instructor: 'Dr. John',
      credits: 4,
      description: 'Learn HTML and CSS from scratch.'
    },
    {
      id: 2,
      name: 'JavaScript',
      instructor: 'Prof. Smith',
      credits: 3,
      description: 'Master JavaScript fundamentals.'
    },
    {
      id: 3,
      name: 'Angular',
      instructor: 'Dr. David',
      credits: 4,
      description: 'Build Angular applications.'
    },
    {
      id: 4,
      name: 'Python',
      instructor: 'Prof. Alex',
      credits: 4,
      description: 'Learn Python programming.'
    }
  ];

  getLocalCourses(): Course[] {
    return this.courses;
  }

  getCourseById(id: number): Course | undefined {
    return this.courses.find(course => course.id === id);
  }

  // ===== Hands-On 10 (Centralized API Layer) =====

  getApiCourses(): Observable<any> {
    return from(getAllCourses());
  }

}