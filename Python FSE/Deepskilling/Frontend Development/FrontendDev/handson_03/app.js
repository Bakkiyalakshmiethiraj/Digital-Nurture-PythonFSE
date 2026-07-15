import { courses } from "./data.js";

const courseContainer = document.getElementById("courseContainer");
const totalCredits = document.getElementById("totalCredits");
const searchBox = document.getElementById("searchBox");
const sortBtn = document.getElementById("sortBtn");

let courseList = [...courses];

function displayCourses(list) {

    courseContainer.innerHTML = "";

    let total = 0;

    list.forEach(course => {

        total += course.credits;

        const card = document.createElement("div");

        card.className = "course-card";

        card.innerHTML = `
            <h3>${course.name}</h3>

            <p><strong>Course Code:</strong> ${course.code}</p>

            <p><strong>Instructor:</strong> ${course.instructor}</p>

            <p>${course.description}</p>

            <span>Credits : ${course.credits}</span>

            <br><br>

            <button class="view-btn" data-id="${course.id}">
                View Details
            </button>
        `;

        courseContainer.appendChild(card);

    });

    totalCredits.textContent = total;

}

displayCourses(courseList);

// Search

searchBox.addEventListener("keyup", () => {

    const text = searchBox.value.toLowerCase();

    const filtered = courseList.filter(course =>
        course.name.toLowerCase().includes(text)
    );

    displayCourses(filtered);

});

// Sort

sortBtn.addEventListener("click", () => {

    courseList.sort((a, b) => a.credits - b.credits);

    displayCourses(courseList);

});

// View Details

courseContainer.addEventListener("click", (event) => {

    if (event.target.classList.contains("view-btn")) {

        const id = Number(event.target.dataset.id);

        const course = courseList.find(c => c.id === id);

        alert(
            `Course: ${course.name}

Code: ${course.code}

Instructor: ${course.instructor}

Credits: ${course.credits}

${course.description}`
        );
    }

});