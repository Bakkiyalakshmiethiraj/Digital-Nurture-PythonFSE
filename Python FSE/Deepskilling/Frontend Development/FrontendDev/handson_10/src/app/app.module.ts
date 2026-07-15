import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import { ErrorHandler } from '@angular/core';


import { courseReducer } from './store/reducers/course.reducer';
import { CourseEffects } from './store/effects/course.effects';
import { GlobalErrorHandlerService } from './services/global-error-handler.service';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { CoursesComponent } from './courses/courses.component';
import { CourseCardComponent } from './course-card/course-card.component';
import { ProfileComponent } from './profile/profile.component';
import { ContactComponent } from './contact/contact.component';
import { CourseListComponent } from './course-list/course-list.component';
import { CourseDetailsComponent } from './course-details/course-details.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { RegistrationComponent } from './registration/registration.component';
import { ApiDemoComponent } from './api-demo/api-demo.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    CoursesComponent,
    CourseCardComponent,
    CourseListComponent,
    ProfileComponent,
    ContactComponent,
    CourseDetailsComponent,
    NotFoundComponent,
    RegistrationComponent,
    ApiDemoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    HttpClientModule,
    ReactiveFormsModule,

    StoreModule.forRoot({
      courses: courseReducer
    }),

    EffectsModule.forRoot([
      CourseEffects
    ])
  ],
  providers: [
     {
    provide: ErrorHandler,
    useClass: GlobalErrorHandlerService
  }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }