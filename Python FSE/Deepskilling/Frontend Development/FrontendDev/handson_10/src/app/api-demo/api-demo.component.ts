import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-api-demo',
  templateUrl: './api-demo.component.html',
  styleUrls: ['./api-demo.component.css']
})
export class ApiDemoComponent implements OnInit {

  users: any[] = [];
  loading = true;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    // Execution stream handshake invocation
    this.apiService.getUsers().subscribe({
      next: (data) => {
        this.users = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('API Middleware Stream Exception:', err);
        this.users = []; // Secure empty boundary array initialization
        this.loading = false;
      }
    });
  }

}