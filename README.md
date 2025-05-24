# STUDY-PAL
StudyPal is a command-line interface (CLI) Python program that helps students efficiently plan and manage their study schedules Designed as the final project for Harvard’s CS50x course, StudyPal offers a structured and intelligent way for learners to divide their syllabus, monitor daily progress, and stay on track with upcoming exams. It removes the hassle of manually calculating what to study each day and ensures steady preparation over time.

## 🎯 Motivation
As students, one of the most challenging aspects of exam preparation is time management and content coverage. Often, students underestimate the effort required and overestimate how much they can do in a short time. This mismatch leads to procrastination, missed topics, and ultimately, poor performance.

StudyPal was created to solve this problem by giving students a lightweight tool to:
- Track subjects and chapters
- Automatically compute how much to study each day
- Visualize progress and completion percentage
- Stay accountable with structured daily goals

Inspired by the principles of spaced repetition and consistent study routines, StudyPal brings practicality and automation together in a minimal interface.

## 🛠 Features

### ✅ Subject Management
Users can add a new subject by providing:
- The subject name (e.g., “Mathematics”)
- Total number of chapters or units
- Exam date in "YYYY-MM-DD" format

Subjects are stored persistently using a JSON file ("data.json").

### ✅ Automatic Schedule Generation
Based on the time remaining until the exam date, StudyPal divides the total chapters over the days left and suggests how many chapters to study each day. If an exam is imminent or the date has passed, StudyPal notifies the user accordingly.

### ✅ Progress Updates
Users can log their daily progress by entering the number of chapters they’ve completed. This is then updated in the database and affects their percentage completion stats.

### ✅ Progress Summary
The tool displays a summary of:
- Chapters completed
- Total chapters
- Percentage completed

### ✅ Persistent Storage
All data is saved in a JSON file, which is automatically loaded and updated. This ensures that users don’t lose their data between sessions.

## 📂 Project Structure
study-pal/
├── project.py # Main CLI program and core functions
├── test_project.py # Pytest-based unit tests
├── requirements.txt # External dependencies (e.g., tabulate)
├── data.json # Persistent storage for study data
└── README.md # This file

## 🧪 Testing
This project includes three testable functions:
- add_subject()
- generate_schedule()
- update_progress()

All of them are covered in "test_project.py" using the "pytest" framework. This ensures that changes and edge cases are automatically caught and verified.

To run tests:
bash:
"pytest test_project.py"

🖥 Usage Instructions
1. Install dependencies:
- pip install -r requirements.txt
2. Run the program:
- python project.py
3. Choose from the menu:
- Add subject
- Generate schedule
- Update progress
- View progress
- Exit
🔧 Technologies Used
- Python 3
- tabulate for CLI tables
- datetime for exam countdown logic
- json for local persistent storage
- pytest for testing

👤 Author
 This project was created by SHRIYA DHAWAN as a final project for CS50x, Harvard University’s Introduction to Computer 
 Science course. I wanted to build something that I personally find useful as a student, and something that reflects real- 
 world needs in a simple, elegant way.

📈 Future Improvements
- Add calendar export for daily study goals
- Send daily reminders via email
- Integrate with Google Calendar API
- Web-based frontend or mobile version
- Gamification and rewards for consistency

📜 License
 This project is open-source and free to use. Feel free to modify and extend it for your own academic use!
