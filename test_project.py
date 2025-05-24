from project import add_subject, generate_schedule, update_progress

def test_add_subject():
    s = add_subject("CS50", 10, "2025-06-15")
    assert s["name"] == "CS50"
    assert s["chapters"] == 10
    assert s["exam_date"] == "2025-06-15"
    assert s["completed"] == 0

def test_generate_schedule():
    subjects = [add_subject("CS50", 10, "2099-12-31")]
    schedule = generate_schedule(subjects)
    assert "CS50" in schedule
    assert isinstance(schedule["CS50"], int)

def test_update_progress():
    data = {"subjects": [add_subject("CS50", 10, "2099-12-31")]}
    updated = update_progress("CS50", 3, data)
    assert updated["subjects"][0]["completed"] == 3
