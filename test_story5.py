from story5 import format_time, generate_schedule


def test_format_time():
    assert format_time(900) == "09:00"
    assert format_time(1330) == "13:30"



def test_generate_valid_schedule():
    schedule = [
        {
            "course": "CS222",
            "section": "002",
            "days": "TR",
            "start": 1300,
            "end": 1400
        },
        {
            "course": "CS120",
            "section": "001",
            "days": "MWF",
            "start": 930,
            "end": 1030
        }
    ]

    result = generate_schedule(schedule)

    assert "CS222" in result
    assert "Section 002" in result
    assert "TR" in result
    assert "13:00-14:00" in result

    assert "CS120" in result
    assert "MWF" in result
    assert "09:30-10:30" in result



def test_generate_no_schedule():
    result = generate_schedule(None)

    assert result == "No valid schedule can be created."