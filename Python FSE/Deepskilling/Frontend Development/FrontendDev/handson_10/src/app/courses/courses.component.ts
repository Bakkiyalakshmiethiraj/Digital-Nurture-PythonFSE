import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent implements OnInit {
  isLoading: boolean = true;
  courses: any[] = [];

  constructor() {}

  ngOnInit(): void {
    // Simulating a real-world asynchronous data fetch
    setTimeout(() => {
      this.courses = [
        { id: '1', name: 'HTML & CSS', instructor: 'Dr. John', credits: 4 },
        { id: '2', name: 'JavaScript', instructor: 'Prof. Smith', credits: 3 },
        { id: '3', name: 'React JS', instructor: 'Dr. David', credits: 4 },
        { id: '4', name: 'Python', instructor: 'Prof. Alex', credits: 4 },
        { id: '5', name: 'Database Systems', instructor: 'Dr. Williams', credits: 3 }
      ];
      this.isLoading = false;
    }, 800);
  }
}