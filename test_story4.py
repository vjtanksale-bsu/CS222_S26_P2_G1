from story4 import is_time_conflict, has_time_conflict


def test_same_day_time_conflict():
    course1 = {
        "days": "MWF",
        "start": 900,
        "end": 1000
    }

    course2 = {
        "days": "MWF",
        "start": 930,
        "end": 1030
    }

    assert is_time_conflict(course1, course2) is True


def test_different_days_no_conflict():
    course1 = {
        "days": "MWF",
        "start": 900,
        "end": 1000
    }

    course2 = {
        "days": "TR",
        "start": 900,
        "end": 1000
    }

    assert is_time_conflict(course1, course2) is False


def test_same_day_no_time_overlap():
    course1 = {
        "days": "MWF",
        "start": 900,
        "end": 1000
    }

    course2 = {
        "days": "MWF",
        "start": 1030,
        "end": 1130
    }

    assert is_time_conflict(course1, course2) is False


def test_multiple_sections_conflict(tmp_path):
    course_file = tmp_path / "courses.txt"

    course_file.write_text(
        "CS222 001 MWF 900 1000\n"
        "CS222 002 TR 1300 1400\n"
        "CS120 001 MWF 930 1030\n"
    )

    files = [str(course_file)]

    selected_courses = ["CS222", "CS120"]

    assert has_time_conflict(selected_courses, files) is True


def test_multiple_sections_no_conflict(tmp_path):
    course_file = tmp_path / "courses.txt"

    course_file.write_text(
        "CS222 001 TR 900 1000\n"
        "CS120 001 MWF 930 1030\n"
    )

    files = [str(course_file)]

    selected_courses = ["CS222", "CS120"]

    assert has_time_conflict(selected_courses, files) is False