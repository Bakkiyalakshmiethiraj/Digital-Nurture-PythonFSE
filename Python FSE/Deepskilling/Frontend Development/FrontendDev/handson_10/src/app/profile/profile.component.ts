import { Component, OnInit } from '@angular/core';
import { EnrollmentService } from '../enrollment.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  // Hardcoded core metrics matching your specific profile info
  studentName: string = 'Bakkiyalakshmi E';
  department: string = 'Information Technology';
  institution: string = 'Saveetha Engineering College';
  academicYear: string = '4th Year';
  cgpa: string = '8.5'; // Adds an elite portfolio placement indicator metric

  constructor(private enrollmentService: EnrollmentService) {}

  ngOnInit(): void {}

  // Reactively pull aggregated calculations from your global store service
  get totalEnrolledCoursesCount(): number {
    return this.enrollmentService.getEnrolledCourses().length;
  }

  get totalEnrolledCredits(): number {
    return this.enrollmentService.getTotalCredits();
  }
}