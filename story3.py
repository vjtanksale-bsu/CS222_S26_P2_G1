def normalize_course(course):
    """Convert input to clean uppercase format."""
    return course.strip().upper()


def is_valid_course(course, available_courses):
    """Check if course exists in available course list."""
    return normalize_course(course) in available_courses


def get_courses_from_user(n, available_courses):
    """
    Collect n valid courses from user input.
    - Reject invalid courses
    - Reject duplicates
    """
    selected = []

    while len(selected) < n:
        course = input(f"Enter course {len(selected)+1}/{n}: ")
        normalized = normalize_course(course)

        # invalid course check
        if normalized not in available_courses:
            print("Invalid course. Not in available list.")
            continue

        # duplicate check
        if normalized in selected:
            print("Duplicate course not allowed.")
            continue

        selected.append(normalized)

    return selected


def select_courses(n, available_courses):
    """Main interface for course selection."""
    return get_courses_from_user(n, available_courses)