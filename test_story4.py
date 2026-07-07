from story4 import parse_course, has_time_conflict

def test_parse_course():
    line = "CS222 574 MWF 1500 1650"
    result = parse_course(line)
    assert result["id"] == "CS222"
    assert result["days"] == "MWF"
    assert result["start"] == 1500
    assert result["end"] == 1650

def test_has_time_conflict_true():
    sample_list = ["CS222 574 MWF 1500 1650", "CS222 996 M 1530 1815"]
    assert has_time_conflict(sample_list) is True

def test_has_time_conflict_false():
    sample_list = ["CS222 574 MWF 1500 1650", "CS222 996 TR 1500 1650"]
    assert has_time_conflict(sample_list) is False