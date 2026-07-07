from story4 import is_time_conflict, find_valid_schedule


def test_same_day_time_conflict():
    """Test overlapping time on same days."""

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
    """Test different meeting days."""

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
    """Test same days but different time."""

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



def test_find_valid_schedule_with_alternative_section(tmp_path):
    """
    Test system can find another section
    when the first section conflicts.
    """

    course_file = tmp_path / "courses.txt"

    course_file.write_text(
        "CS222 001 MWF 900 1000\n"
        "CS222 002 TR 1300 1400\n"
        "CS120 001 MWF 930 1030\n"
    )

    files = [str(course_file)]

    selected_courses = [
        "CS222",
        "CS120"
    ]

    result = find_valid_schedule(
        selected_courses,
        files
    )

    assert result is not None

    assert result[0]["course"] == "CS222"
    assert result[0]["section"] == "002"

    assert result[1]["course"] == "CS120"



def test_no_valid_schedule(tmp_path):
    """
    Test when all sections have conflicts.
    """

    course_file = tmp_path / "courses.txt"

    course_file.write_text(
        "CS222 001 MWF 900 1400\n"
        "CS222 002 MWF 900 1400\n"
        "CS120 001 MWF 930 1030\n"
        "CS120 002 MWF 1130 1230\n"
    )

    files = [str(course_file)]

    selected_courses = [
        "CS222",
        "CS120"
    ]

    result = find_valid_schedule(
        selected_courses,
        files
    )

    assert result is None