from story1 import extract_course_numbers, get_all_available_courses

# Unit Test 1
def test_extract_course_numbers():
    lines = [
        "CS222 574 MWF 1500 1650",
        "CS222 996 TR 1530 1815",
        "CS120 292 MWF 1800 1850"
    ]

    result = extract_course_numbers(lines)

    assert "CS222" in result
    assert "CS120" in result
    assert len(result) == 2


# Unit Test 2 (multi-file test)
def test_get_all_available_courses():
    files = ["courses.txt", "courses1.txt", "courses2.txt"]

    result = get_all_available_courses(files)

    assert isinstance(result, list)
    assert len(result) > 0

    assert "CS222" in result
    assert "CS120" in result or "CS121" in result


# Unit Test 3 (no duplicates)
def test_no_duplicates():
    lines = [
        "CS222 574 MWF 1500 1650",
        "CS222 996 MWF 1530 1815",
        "CS222 123 TR 1000 1100"
    ]

    result = extract_course_numbers(lines)

    assert result == ["CS222"]