import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {

  constructor(private fb: FormBuilder) {}

  registrationForm = this.fb.group({
    name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    course: ['', Validators.required]
  });

  onSubmit() {
    if (this.registrationForm.valid) {
      alert('Registration Successful!');
      console.log(this.registrationForm.value);
      this.registrationForm.reset();
    }
  }
}