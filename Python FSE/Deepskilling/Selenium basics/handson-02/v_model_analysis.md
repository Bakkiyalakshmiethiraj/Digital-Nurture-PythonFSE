### Hands-On 2
### SDLC vs TDLC – V-Model & Agile QA Integration
### Task 1: V-Model Mapping
### 1. V-Model Diagram
                 SDLC (Development)

          Requirements
                |
                |
          System Design
                |
                |
       Architecture Design
                |
                |
          Module Design
                |
                |
              Coding
                |
                |
        -----------------
        |               |
    Unit Testing     Module Design
        |
Integration Testing  Architecture Design
        |
 System Testing      System Design
        |
Acceptance Testing   Requirements

The V-Model shows that every development phase has a corresponding testing phase. Testing activities are planned early, even before coding begins.

### 2. SDLC Phase ↔ TDLC Phase Mapping
SDLC Phase	Corresponding TDLC Phase	Test Artifact Produced
Requirements	Acceptance Testing	Acceptance Test Plan, Acceptance Test Cases
System Design	System Testing	System Test Plan, System Test Cases
Architecture Design	Integration Testing	Integration Test Plan and Test Cases
Module Design	Unit Testing	Unit Test Cases
Coding	Execution of all Tests	Source Code
### 3. Entry Criteria and Exit Criteria
Unit Testing

Entry Criteria

Module development completed
Source code available
Unit test cases prepared

Exit Criteria

All unit test cases executed
All critical defects fixed
Code coverage achieved
Integration Testing

Entry Criteria

Unit testing completed successfully
Modules integrated
Integration test cases ready

Exit Criteria

Integration test cases passed
Interfaces working correctly
No major integration defects
System Testing

Entry Criteria

Complete application deployed
Integration testing completed
Test environment ready

Exit Criteria

All system test cases executed
Critical and high-severity defects resolved
Application meets functional requirements
Acceptance Testing (UAT)

Entry Criteria

System testing completed
Product ready for business validation
Acceptance test cases approved

Exit Criteria

Business users approve the application
Acceptance criteria satisfied
Product ready for production deployment
### 4. Early QA Engagement in the Course Management API Project
Requirements Review

QA reviews the requirements to identify ambiguities, missing validations, and unclear business rules before development starts.

Design Review

QA reviews the system design and API specifications to prepare test cases, identify possible risks, and ensure the design is testable.

Task 2: Agile QA and Shift-Left Testing
### 5. Problems with Waterfall Testing
Problem 1

Defects are discovered very late, making them more expensive and time-consuming to fix.

Problem 2

Requirement misunderstandings remain unnoticed until testing begins, causing major rework.

Problem 3

Development and QA teams work separately, resulting in poor communication and delayed project delivery.

### 6. QA Role in Agile Ceremonies
Sprint Planning
Understand user stories
Define acceptance criteria
Estimate testing effort
Identify test scenarios
Daily Stand-up
Share testing progress
Report blocked issues
Discuss defects with developers
Coordinate testing activities
Sprint Review
Validate completed features
Perform demonstration testing
Confirm acceptance criteria are met
Collect stakeholder feedback
Retrospective
Discuss testing challenges
Suggest process improvements
Improve collaboration
Plan better testing strategies for the next sprint
### 7. Shift-Left Testing Practices
a) Reviewing Requirements for Testability

QA reviews requirements before development starts to ensure they are complete, clear, and testable.

b) Writing Test Cases Before Code (TDD/BDD)

QA prepares test cases and scenarios before coding begins so developers clearly understand expected behavior.

c) Static Code Analysis

Developers use static analysis tools to identify coding issues, security vulnerabilities, and coding standard violations before execution.

d) API Contract Testing Before Integration

QA validates API request and response formats using the API contract before integrating different modules, preventing integration failures.

### 8. Acceptance Criteria (Given–When–Then)
Scenario 1 – Happy Path

Given the college admin is on the Create Course page

When the admin enters a valid course name and course code and clicks Submit

Then the course should be created successfully and displayed in the course list.

Scenario 2 – Duplicate Course Code

Given a course with the same course code already exists

When the admin submits the form using the duplicate course code

Then the system should display an error message stating that the course code already exists and should not create the course.

Scenario 3 – Missing Required Fields

Given the admin leaves one or more mandatory fields empty

When the admin clicks Submit

Then the system should display validation error messages and prevent course creation.

### Conclusion

The V-Model connects every development phase with its corresponding testing phase, ensuring early test planning and better software quality. Agile integrates QA throughout the development lifecycle, while Shift-Left Testing promotes early defect detection through requirement reviews, early test case creation, static code analysis, and API contract testing. This approach reduces development cost, improves collaboration, and delivers reliable software more efficiently.