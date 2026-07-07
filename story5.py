def format_time(time):
    """Convert time format for display."""
    hour = time // 100
    minute = time % 100

    return f"{hour:02d}:{minute:02d}"


def generate_schedule(schedule):
    """
    Generate final schedule output.
    """

    if schedule is None:
        return "No valid schedule can be created."

    result = []

    for course in schedule:
        result.append(
            f"{course['course']} "
            f"Section {course['section']} "
            f"{course['days']} "
            f"{format_time(course['start'])}-"
            f"{format_time(course['end'])}"
        )

    return "\n".join(result)