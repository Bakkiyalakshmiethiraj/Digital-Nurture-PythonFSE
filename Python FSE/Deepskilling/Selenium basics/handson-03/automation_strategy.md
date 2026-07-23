### Hands-On 3
Test Automation Process, Lifecycle & Framework Types
Task 1: Automation Decision and Test Case Selection
### 1. Criteria for Deciding Whether a Test Case Should Be Automated
Criterion 1: Repetitive Execution

Tests that are executed frequently are good candidates for automation.

Application:
The POST /api/courses/ endpoint is tested after every code change, making it suitable for automation.

Criterion 2: Regression Testing

Regression tests ensure that existing functionality continues to work after new changes.

Application:
Automating the course creation API helps verify that updates do not break existing functionality.

Criterion 3: Stable Functionality

Features that rarely change are ideal for automation because scripts require less maintenance.

Application:
The API endpoint for creating courses is stable and follows a fixed request and response format.

Criterion 4: Data-Driven Testing

Tests requiring multiple input combinations are easier and faster to automate.

Application:
Different course names, codes, and descriptions can be tested automatically using various datasets.

Criterion 5: High Business Importance

Critical business features should always be automated to reduce risk.

Application:
Course creation is a core feature of the Course Management System, making automation highly valuable.

### 2. Automate or Manual
Test Case	Decision	Justification
Regression test for all CRUD endpoints after every code change	Automate	Executed frequently and saves significant manual effort.
Exploratory testing of a new search feature	Manual	Requires human observation and creativity.
Performance test with 100 concurrent users	Automate	Performance tools can simulate multiple users efficiently.
UI test for the login form	Automate	Frequently executed during regression testing.
Verify Swagger API documentation	Manual	Requires checking readability, completeness, and accuracy.
Smoke test after deployment	Automate	Quickly verifies that the application is available after deployment.
### 3. Test Automation ROI
Definition

Return on Investment (ROI) in test automation measures whether the time and cost spent creating automated tests are recovered through reduced manual testing effort.

Calculation

Time to automate one regression test = 4 hours

Manual execution time = 30 minutes = 0.5 hours

Break-even point:

4 ÷ 0.5 = 8 runs

Therefore, automation pays for itself after approximately 8 executions.

After the 10th run, a maintenance overhead of 20% is added.

Maintenance time per run:

20% of 0.5 hour = 0.1 hour

Effective savings per run after maintenance:

0.5 − 0.1 = 0.4 hour

Even with maintenance, automation continues to save time for every future execution.

### 4. Flaky Tests
Definition

A flaky test is a test that sometimes passes and sometimes fails without any changes to the application code.

Example

A Selenium test clicks a button immediately after page loading without waiting for it to become clickable. Sometimes it passes, while other times it fails because the element has not finished loading.

Strategies to Prevent Flaky Tests
Use Explicit Waits instead of time.sleep().
Use stable and unique locators such as ID or CSS Selectors.
Ensure test data and the test environment remain consistent before execution.
Task 2: Compare Automation Framework Types
### 5. Automation Framework Comparison
Linear Framework

Description

The Linear Framework, also called the Record-and-Playback Framework, executes test cases sequentially without separating test logic or reusable components.

Advantage

Easy to create and understand.

Disadvantage

Difficult to maintain for large projects.

Course Management Example

Automating a single login test for demonstration purposes.

Modular Framework

Description

The application is divided into reusable modules, and each module has its own test script.

Advantage

Reusable and easier to maintain.

Disadvantage

Initial setup requires more planning.

Course Management Example

Separate modules for Login, Course Management, Student Management, and Reports.

Data-Driven Framework

Description

Test data is stored externally (Excel, CSV, JSON, etc.), allowing one script to execute multiple test scenarios.

Advantage

Executes the same test with different input values.

Disadvantage

Managing external test data adds complexity.

Course Management Example

Testing course creation using multiple course names and course codes stored in an Excel file.

Keyword-Driven Framework

Description

Tests are created using predefined keywords such as Login, Click, EnterText, and Verify.

Advantage

Non-technical users can create test cases.

Disadvantage

Framework design and maintenance are more complex.

Course Management Example

Business analysts prepare keyword-based test cases without writing Selenium code.

Hybrid Framework

Description

The Hybrid Framework combines Modular, Data-Driven, and Keyword-Driven approaches to provide flexibility, reusability, and maintainability.

Advantage

Highly scalable and suitable for large enterprise applications.

Disadvantage

Requires experienced automation engineers to design and maintain.

Course Management Example

A Selenium framework where reusable page objects, Excel test data, utility classes, and reusable keywords work together.

### 6. Recommended Framework
Recommendation

For the Course Management frontend, I recommend a Hybrid Framework combining Modular, Data-Driven, and Keyword-Driven approaches.

Justification
Login functionality can be reused across more than 20 test cases using modular components.
Fifty different username/password combinations can be tested using data-driven testing.
Non-technical team members can create keyword-based test cases without programming knowledge.
The framework is scalable, maintainable, and widely used in enterprise automation projects.
### 7. Hybrid Framework Folder Structure
CourseManagementAutomation/
│
├── config/
│   ├── config.py
│   └── settings.json
│
├── test_data/
│   ├── login_data.xlsx
│   ├── courses.csv
│   └── users.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── course_page.py
│   └── dashboard_page.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   ├── wait_utils.py
│   └── screenshot.py
│
├── tests/
│   ├── test_login.py
│   ├── test_course.py
│   └── test_dashboard.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── requirements.txt
└── README.md
### Folder Description
config/ – Stores configuration files such as URLs, browser settings, and environment variables.
test_data/ – Contains external test data (Excel, CSV, JSON).
pages/ – Implements the Page Object Model, where page elements and actions are defined.
utilities/ – Includes reusable helper functions such as WebDriver setup, logging, waits, and screenshots.
tests/ – Contains all Selenium test scripts.
reports/ – Stores HTML reports and failure screenshots.
requirements.txt – Lists all Python dependencies.
README.md – Provides project documentation and execution instructions.
### Conclusion

Test automation helps improve software quality by reducing manual effort, increasing test coverage, and supporting continuous testing. Selecting the right test cases for automation and choosing an appropriate framework are essential for building reliable automation suites. Among all framework types, the Hybrid Framework is the most suitable for enterprise applications because it combines reusability, scalability, maintainability, and support for both technical and non-technical team members.