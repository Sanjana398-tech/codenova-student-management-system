

# 🎓 Student Record Management System

A web-based Student Record Management System built using Python, Flask, and SQLite. It provides an interactive dashboard for managing student information, tracking academic performance, and viewing GPA statistics.

## 🌐 Live Demo

**Live Website:** https://codenova-student-management-system.onrender.com

## 📌 About the Project

The Student Record Management System is designed to simplify student record management through a clean, interactive web interface. It allows users to add, view, search, update, and delete student records while displaying academic statistics through a dashboard.

The project demonstrates Python programming, database integration, web development, input validation, and basic data visualization.

## ✨ Features

* ➕ **Add Students:** Add student details, including roll number, name, email, and GPA.
* 📋 **View Records:** Display student records in a structured table.
* 🔍 **Search Students:** Search records by student name, roll number, or email.
* ✏️ **Update Records:** Modify existing student information.
* 🗑️ **Delete Records:** Remove student records with confirmation.
* 📊 **GPA Dashboard:** View student statistics and GPA distribution.
* 🌙 **Dark Mode:** Switch between light and dark themes.
* 🎨 **Interactive UI:** Responsive layout with animations and visual feedback.
* ✅ **Input Validation:** Validate student details before saving records.
* 💾 **Database Integration:** Store student information using SQLite.

## 🛠️ Technologies Used

| Technology   | Purpose                                    |
| ------------ | ------------------------------------------ |
| Python       | Application logic                          |
| Flask        | Web framework                              |
| SQLite       | Database management                        |
| HTML5        | Webpage structure                          |
| CSS3         | Styling, animations, and responsive design |
| JavaScript   | Interactive features                       |
| Chart.js     | GPA chart visualization                    |
| Git & GitHub | Version control and source code hosting    |
| Render       | Web application deployment                 |

## 📂 Project Structure

```text
Student_Record_Management_System/
│
├── web_app.py
├── main.py
├── database.py
├── models.py
├── validators.py
├── student_service.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── tests/
├── data/
│   └── students.db
│
├── .gitignore
└── README.md
```

*Note: The files and folders shown above represent the expected structure. Adjust them to match your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Student_Record_Management_System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python web_app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🧪 Testing

The project includes a `tests/` directory for testing application functionality.

Run the tests using the appropriate test runner and dependencies configured in your project.

For example, if your tests use pytest:

```bash
python -m pytest
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Developing web applications using Flask.
* Implementing CRUD operations.
* Integrating SQLite with Python.
* Validating user inputs.
* Building interactive dashboards.
* Visualizing academic statistics.
* Managing source code using Git and GitHub.
* Deploying a web application using Render.

## 🚀 Future Improvements

* Add authentication and role-based access.
* Export student records to CSV or Excel.
* Improve database backup and persistence.
* Add pagination for large student datasets.
* Expand dashboard analytics.

## 👩‍💻 Author

**Sanjana N. Naik**

Computer Science and Engineering Student | Python Developer | AI & Cybersecurity Enthusiast

---

## Step 2: Add your actual links

Before committing, replace these placeholders:

* `Add Your Render Website URL Here` with your actual Render URL.
* `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

For example, your links will look like this:

```text
https://your-project-name.onrender.com
https://github.com/your-username/Student-Record-Management-System
```

These are examples only; use your real links.

## Step 3: Upload the README to GitHub

In the VS Code terminal, run:

```bash
git add README.md
git commit -m "Add project documentation"
git push
```

Then refresh your GitHub repository page. Your README should appear on the repository's front page.

**Important:** Your application uses SQLite, so verify how the database is initialized and persisted on Render before claiming that records are permanently stored.

---

### Next, let's make your repository even better! 🚀

After you add the README, we can add **screenshots of your deployed dashboard** so recruiters can see the interface without opening the application.
