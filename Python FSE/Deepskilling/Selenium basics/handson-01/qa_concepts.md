# Hands-On 1

## Task 1

### Unit Testing

Test the create_course() function with valid course data.

Input

Course Name : Python

Course Code : PY101

Expected Result

Course should be created successfully.

Type

Functional Testing

### Integration Testing

Verify that POST /api/courses/

stores the course in the database successfully.

Expected Result

HTTP 201 Created

Database contains the course.

### System Testing

Create a course.

Retrieve it.

Verify it appears in the course list.

Expected Result

Complete workflow works correctly.

### User Acceptance Testing

College Admin creates a course.

Expected Result

Course is visible and students can enroll.

Non Functional Example

Performance Testing

Verify that 1000 users can create courses simultaneously.

Expected Result

Response time less than 2 seconds.

Black Box

QA Tester

Checks only inputs and outputs.

White Box

Developer

Checks internal code.


| Test Case ID | Description                            | Preconditions                       | Test Steps                                        | Expected Result                                      | Actual Result | Pass/Fail |
| ------------ | -------------------------------------- | ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------- | ------------- | --------- |
| TC_001       | Create course with valid data          | API is running, database connected  | Send POST request with valid course name and code | Course created successfully with HTTP 201            |               |           |
| TC_002       | Create course with missing course name | API is running                      | Send POST request without course name             | API should return HTTP 400 validation error          |               |           |
| TC_003       | Create duplicate course code           | Existing course code already exists | Send POST request with existing course code       | API should reject duplicate and return error message |               |           |


### Task 2: Defect Lifecycle & Severity Classification

### Defect Lifecycle

New
 |
 v
Assigned
 |
 v
Open
 |
 v
Fixed
 |
 v
Retest
 |
 v
Verified
 |
 v
Closed


Rejected:
New → Rejected
(Developer rejects because it is not a valid defect)


Deferred:
New/Open → Deferred
(Fix postponed to future release)

### 6. Severity and Priority Classification

| Bug                                                   | Severity | Priority | Reason                                        |
| ----------------------------------------------------- | -------- | -------- | --------------------------------------------- |
| POST /api/courses/ returns 500 error for all requests | Critical | P1       | Core API functionality is unavailable         |
| Course names above 150 characters silently truncate   | Medium   | P2       | Data loss occurs but system works             |
| Swagger documentation typo                            | Low      | P4       | Only documentation issue                      |
| Login occasionally returns 401                        | High     | P1       | Affects user access and indicates instability |



### Defect Report

Defect ID:
BUG_API_001

Title:
POST /api/courses/ returns 500 Internal Server Error

Environment:
Testing Environment

Build Version:
v1.0

Severity:
Critical

Priority:
P1

Steps to Reproduce:

1. Open API client
2. Send POST request to /api/courses/
3. Provide valid course details
4. Submit request

Expected Result:

API should create course successfully and return HTTP 201 Created.

Actual Result:

API returns HTTP 500 Internal Server Error.

Attachments:

Screenshot of 500 error

### Severity vs Priority Difference

Severity describes the impact of a defect on the system.

Priority describes how quickly the defect should be fixed.

Example:

A spelling mistake on the CEO dashboard:
Severity: Low
Priority: High

Because technically it does not break the system, but it affects an important stakeholder.