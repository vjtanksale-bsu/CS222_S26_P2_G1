def normalize_course(course):
    return course.strip().upper()


def is_valid_course(course, available_courses):
    return normalize_course(course) in available_courses


def get_courses_from_user(n, available_courses):
    selected = []

    while len(selected) < n:
        course = input(f"Enter course {len(selected)+1}/{n}: ")
        normalized = normalize_course(course)

        if normalized not in available_courses:
            print("Invalid course. Not in available list.")
            continue

        if normalized in selected:
            print("Duplicate course not allowed.")
            continue

        selected.append(normalized)

    return selected


def select_courses(n, available_courses):
    return get_courses_from_user(n, available_courses)

