/*
NgRx Data Flow

Component
   ↓
Dispatch Action
   ↓
Effect
   ↓
CourseService (API)
   ↓
Reducer
   ↓
Store (State)
   ↓
Selector
   ↓
Component
*/

import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { CourseService } from '../../services/course.service';
import * as CourseActions from '../actions/course.actions';
import { catchError, map, mergeMap } from 'rxjs/operators';
import { of } from 'rxjs';

@Injectable()
export class CourseEffects {

  loadCourses$ = createEffect(() =>
    this.actions$.pipe(
      ofType(CourseActions.loadCourses),
      mergeMap(() =>
        this.courseService.getApiCourses().pipe(
          map(courses =>
            CourseActions.loadCoursesSuccess({ courses })
          ),
          catchError(error =>
            of(CourseActions.loadCoursesFailure({ error }))
          )
        )
      )
    )
  );

  constructor(
    private actions$: Actions,
    private courseService: CourseService
  ) {}

}