from story3 import is_valid_course, has_no_duplicates


def test_valid_course():
    available = ["CS222", "CS120"]
    assert is_valid_course("CS222", available) is True


def test_invalid_course():
    available = ["CS222", "CS120"]
    assert is_valid_course("CS999", available) is False


def test_no_duplicates_true():
    assert has_no_duplicates(["CS222", "CS120"]) is True


def test_no_duplicates_false():
    assert has_no_duplicates(["CS222", "CS222"]) is False