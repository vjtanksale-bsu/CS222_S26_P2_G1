from story2 import is_valid_course_count, parse_course_count


def test_valid_input():
    assert is_valid_course_count("1") == True
    assert is_valid_course_count("7") == True
    assert is_valid_course_count("3") == True


def test_invalid_input_out_of_range():
    assert is_valid_course_count("0") == False
    assert is_valid_course_count("8") == False
    assert is_valid_course_count("10") == False


def test_invalid_input_type():
    assert is_valid_course_count("abc") == False
    assert is_valid_course_count("-1") == False
    assert is_valid_course_count("2.5") == False


def test_parse_course_count():
    assert parse_course_count("5") == 5