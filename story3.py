def normalize_course(course):
    """Clean input."""
    return course.strip().upper()


def is_valid_course(course, available_courses):
    """Check course exists."""
    return normalize_course(course) in available_courses


def get_courses_from_user(n, available_courses):
    """Get n valid courses."""
    selected = []

    while len(selected) < n:
        course = input(f"Enter course {len(selected)+1}/{n}: ")
        normalized = normalize_course(course)

        if not is_valid_course(course, available_courses):
            print("Invalid course.")
            continue

        if normalized in selected:
            print("Duplicate course.")
            continue

        selected.append(normalized)

    return selected


def select_courses(n, available_courses):
    """Start selection."""
    return get_courses_from_user(n, available_courses)