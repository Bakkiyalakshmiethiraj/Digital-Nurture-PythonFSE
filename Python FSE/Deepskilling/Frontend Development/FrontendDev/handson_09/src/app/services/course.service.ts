import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Course } from '../models/course';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor(private http: HttpClient) {}

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

  // ===== Hands-On 8 (HTTP Client) =====

  private apiUrl = 'https://jsonplaceholder.typicode.com/users';

  getApiCourses(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

}