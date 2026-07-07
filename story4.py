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

                        # Store all sections of the same course
                        if course_number not in courses:
                            courses[course_number] = []

                        courses[course_number].append(course)

        except FileNotFoundError:
            continue

    return courses


def is_time_conflict(course1, course2):
    """Check if two sections have overlapping time."""

    # Check if the two courses meet on the same days
    same_days = set(course1["days"]) & set(course2["days"])

    if not same_days:
        return False

    # Check if their time intervals overlap
    time_overlap = (
        max(course1["start"], course2["start"])
        <
        min(course1["end"], course2["end"])
    )

    return time_overlap


def has_time_conflict(selected_courses, files):
    """Check conflicts between selected courses."""

    course_data = read_course_data(files)

    # Compare every pair of selected courses
    for i in range(len(selected_courses)):
        for j in range(i + 1, len(selected_courses)):

            course1_sections = course_data.get(
                selected_courses[i], []
            )

            course2_sections = course_data.get(
                selected_courses[j], []
            )

            # Check every possible section combination
            for section1 in course1_sections:
                for section2 in course2_sections:

                    if is_time_conflict(section1, section2):
                        return True

    return False