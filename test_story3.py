from story3 import is_valid_course, select_courses


def test_valid_course():
    available = ["CS222", "CS120"]

    assert is_valid_course("cs222", available) is True
    assert is_valid_course("CS120", available) is True


def test_invalid_course():
    available = ["CS222", "CS120"]

    assert is_valid_course("CS999", available) is False


def test_select_courses(monkeypatch):
    available = ["CS222", "CS120"]

    inputs = iter(["cs222", "CS120"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = select_courses(2, available)

    assert result == ["CS222", "CS120"]