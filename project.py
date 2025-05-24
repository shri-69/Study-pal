import json
from datetime import datetime, timedelta
from tabulate import tabulate

DATA_FILE = "data.json"

def main():
    data = load_data()

    while True:
        print("\n📚 StudyPal - Smart Study Planner")
        print("1. Add a subject")
        print("2. Generate study schedule")
        print("3. Update progress")
        print("4. View progress")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Subject name: ").strip()
            chapters = int(input("Number of chapters: ").strip())
            exam_date = input("Exam date (YYYY-MM-DD): ").strip()
            subject = add_subject(name, chapters, exam_date)
            data["subjects"].append(subject)
            save_data(data)
        elif choice == "2":
            schedule = generate_schedule(data["subjects"])
            data["schedule"] = schedule
            print(tabulate(schedule.items(), headers=["Subject", "Daily Chapters"]))
            save_data(data)
        elif choice == "3":
            subject = input("Enter subject name: ").strip()
            completed = int(input("Chapters completed: ").strip())
            data = update_progress(subject, completed, data)
            save_data(data)
        elif choice == "4":
            view_progress(data)
        elif choice == "5":
            print("Good luck with your studies! 📘")
            break
        else:
            print("Invalid choice. Try again.")

def add_subject(name: str, chapters: int, exam_date: str) -> dict:
    return {
        "name": name,
        "chapters": chapters,
        "exam_date": exam_date,
        "completed": 0
    }

def generate_schedule(subjects: list) -> dict:
    schedule = {}
    for subject in subjects:
        days_remaining = (datetime.strptime(subject["exam_date"], "%Y-%m-%d") - datetime.now()).days
        if days_remaining > 0:
            daily = max(1, round(subject["chapters"] / days_remaining))
            schedule[subject["name"]] = daily
        else:
            schedule[subject["name"]] = "Exam Over or Today"
    return schedule

def update_progress(subject: str, chapters_completed: int, data: dict) -> dict:
    for s in data["subjects"]:
        if s["name"].lower() == subject.lower():
            s["completed"] += chapters_completed
            return data
    return data

def view_progress(data: dict):
    print("\n📈 Progress Summary:")
    table = []
    for s in data["subjects"]:
        percentage = (s["completed"] / s["chapters"]) * 100 if s["chapters"] > 0 else 0
        table.append([s["name"], s["completed"], s["chapters"], f"{percentage:.2f}%"])
    print(tabulate(table, headers=["Subject", "Completed", "Total", "Progress"]))

def save_data(data: dict):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data() -> dict:
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"subjects": [], "schedule": {}}
