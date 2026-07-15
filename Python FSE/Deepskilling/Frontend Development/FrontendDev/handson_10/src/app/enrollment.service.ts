import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EnrollmentService {
  // Array tracking all currently enrolled course objects
  private enrolledCourses: any[] = [];

  constructor() {}

  getEnrolledCourses() {
    return this.enrolledCourses;
  }

  // Calculate combined academic value reactively
  getTotalCredits(): number {
    return this.enrolledCourses.reduce((sum, course) => sum + course.credits, 0);
  }

  isEnrolled(courseId: string): boolean {
    return this.enrolledCourses.some(c => c.id === courseId);
  }

  enroll(course: any) {
    if (!this.isEnrolled(course.id)) {
      this.enrolledCourses.push(course);
    }
  }

  withdraw(courseId: string) {
    this.enrolledCourses = this.enrolledCourses.filter(c => c.id !== courseId);
  }
}