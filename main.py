from story1 import get_all_available_courses
from story2 import get_course_count
from story3 import select_courses
from story4 import find_valid_schedule


# Course files
files = [
    "courses.txt",
    "courses1.txt",
    "courses2.txt"
]


# Story 1: Get available courses
available_courses = get_all_available_courses(files)

print("Available courses:")
print(available_courses)


# Story 2: Get number of courses
max_n = len(available_courses)

n = get_course_count(max_n)

print(f"\nYou need to select {n} courses.")


# Story 3: Select courses
selected_courses = select_courses(
    n,
    available_courses
)

print("\nSelected courses:")
print(selected_courses)


# Story 4: Find valid sections
schedule = find_valid_schedule(
    selected_courses,
    files
)


if schedule is None:
    print("\nNo valid schedule found.")
else:
    print("\nValid schedule:")

    for course in schedule:
        print(
            f"{course['course']} "
            f"Section {course['section']} "
            f"{course['days']} "
            f"{course['start']}-{course['end']}"
        )