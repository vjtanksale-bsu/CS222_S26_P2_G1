from story3 import is_valid_course, select_courses


def test_valid_course():
    available = ["CS222", "CS120"]

    assert is_valid_course("cs222", available)
    assert is_valid_course("CS120", available)


def test_invalid_course():
    available = ["CS222", "CS120"]

    assert not is_valid_course("CS999", available)


def test_select_courses(monkeypatch):
    available = ["CS222", "CS120"]

    inputs = iter(["cs222", "CS120"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = select_courses(2, available)

    assert result == ["CS222", "CS120"]
    assert len(result) == 2

def test_user_cannot_enter_same_course_more_than_once(monkeypatch, capsys):
    available_courses = ["CS120", "CS222"]
    inputs = iter(["CS222", "cs222", "CS120"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = select_courses(2, available_courses)

    assert result == ["CS222", "CS120"]
    assert "Duplicate course." in capsys.readouterr().out