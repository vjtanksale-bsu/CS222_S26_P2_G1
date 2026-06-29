from story2 import is_valid_course_count, parse_course_count


def test_valid_range():
    assert is_valid_course_count("1", 5) is True
    assert is_valid_course_count("5", 5) is True


def test_invalid_range():
    assert is_valid_course_count("0", 5) is False
    assert is_valid_course_count("6", 5) is False


def test_invalid_input():
    assert is_valid_course_count("abc", 5) is False
    assert is_valid_course_count("", 5) is False


def test_parse_course_count():
    assert parse_course_count("3") == 3