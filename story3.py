def is_valid_course(course, available_courses):
    return course in available_courses


def has_no_duplicates(course_list):
    return len(course_list) == len(set(course_list))


def get_courses_from_user(n, available_courses):
    selected = []

    while len(selected) < n:
        course = input(f"Enter course {len(selected)+1}/{n}: ").strip()

        if not is_valid_course(course, available_courses):
            print("Invalid course. Not in available list.")
            continue

        if course in selected:
            print("Duplicate course not allowed.")
            continue

        selected.append(course)

    return selected


def select_courses(n, available_courses):
    return get_courses_from_user(n, available_courses)


