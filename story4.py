def parse_course(line):
    """Extract course information from one line."""
    parts = line.strip().split()

    return {
        "course": parts[0],
        "section": parts[1],
        "days": parts[2],
        "start": int(parts[3]),
        "end": int(parts[4])
    }


def read_course_data(files):
    """Read course sections from files."""
    courses = {}

    for filename in files:
        try:
            with open(filename, "r") as file:
                for line in file:
                    if line.strip():
                        course = parse_course(line)

                        course_number = course["course"]

                        if course_number not in courses:
                            courses[course_number] = []

                        courses[course_number].append(course)

        except FileNotFoundError:
            continue

    return courses


def is_time_conflict(course1, course2):
    """Check if two sections have time conflict."""

    # Check same meeting days
    same_days = set(course1["days"]) & set(course2["days"])

    if not same_days:
        return False

    # Check overlapping time
    return (
        max(course1["start"], course2["start"])
        <
        min(course1["end"], course2["end"])
    )


def find_valid_schedule(selected_courses, files):
    """
    Find sections without time conflicts.
    Return valid section combination.
    """

    course_data = read_course_data(files)

    selected_sections = []

    def backtrack(index):
        # All courses have assigned sections
        if index == len(selected_courses):
            return True

        course = selected_courses[index]

        sections = course_data.get(course, [])

        for section in sections:

            conflict = False

            # Check this section with previous selections
            for selected in selected_sections:
                if is_time_conflict(section, selected):
                    conflict = True
                    break

            # Try next section if conflict exists
            if conflict:
                continue

            # Choose this section
            selected_sections.append(section)

            if backtrack(index + 1):
                return True

            # Remove if it does not work
            selected_sections.pop()

        return False


    if backtrack(0):
        return selected_sections

    return None