import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  registrationForm!: FormGroup;
  showSuccessPopup: boolean = false; // 🌟 Logic flag to manage modal overlay

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.registrationForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      course: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.registrationForm.valid) {
      // 🌟 Spawns your creative green validation confirmation popup layout
      this.showSuccessPopup = true;
    }
  }

  dismissPopup(): void {
    this.showSuccessPopup = false;
    this.registrationForm.reset({ course: '' }); // Reinitialize form input matrices clean
  }
}