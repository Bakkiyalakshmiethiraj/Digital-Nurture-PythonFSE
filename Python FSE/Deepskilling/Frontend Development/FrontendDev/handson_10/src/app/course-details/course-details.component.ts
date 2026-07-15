import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router'; // 🌟 Inject ActivatedRoute to read URL parameters
import { EnrollmentService } from '../enrollment.service';

@Component({
  selector: 'app-course-details',
  templateUrl: './course-details.component.html',
  styleUrls: ['./course-details.component.css']
})
export class CourseDetailsComponent implements OnInit {
  course: any;
  showSuccessPopup: boolean = false;

  // Mock Database Array matching your 5 core course registry cards exactly
  private courseDatabase = [
    { id: '1', name: 'HTML & CSS', instructor: 'Dr. John', credits: 4 },
    { id: '2', name: 'JavaScript', instructor: 'Prof. Smith', credits: 3 },
    { id: '3', name: 'React JS', instructor: 'Dr. David', credits: 4 },
    { id: '4', name: 'Python', instructor: 'Prof. Alex', credits: 4 },
    { id: '5', name: 'Database Systems', instructor: 'Dr. Williams', credits: 3 }
  ];

  constructor(
    private route: ActivatedRoute,             // 🌟 Injected Route tracking asset
    private enrollmentService: EnrollmentService
  ) {}

  ngOnInit(): void {
    // 🌟 1. Extract the active path parameter target string id from the URL mapping
    const courseId = this.route.snapshot.paramMap.get('id');

    // 🌟 2. Look up the item matching that ID from our database matrix records array
    this.course = this.courseDatabase.find(c => c.id === courseId);

    // Fallback error routing logic safeguard in case the user enters a bad URL
    if (!this.course) {
      this.course = { name: 'Course Not Found', instructor: 'Unknown', credits: 0 };
    }
  }

  get enrolled(): boolean {
    return this.course ? this.enrollmentService.isEnrolled(this.course.id) : false;
  }

  get totalEnrolledCredits(): number {
    return this.enrollmentService.getTotalCredits();
  }

  handleEnrollmentToggle(): void {
    if (!this.course || this.course.credits === 0) return;

    if (this.enrolled) {
      this.enrollmentService.withdraw(this.course.id);
    } else {
      this.enrollmentService.enroll(this.course);
      this.showSuccessPopup = true;
    }
  }

  closePopup(): void {
    this.showSuccessPopup = false;
  }
}