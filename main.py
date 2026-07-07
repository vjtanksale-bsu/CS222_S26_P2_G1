from story1 import get_all_available_courses
from story2 import get_course_count
from story3 import select_courses
from story4 import find_valid_schedule
from story5 import generate_schedule
import os


def get_course_file():
    """Get valid course file from user."""

    available_files = [
        "courses.txt",
        "courses1.txt",
        "courses2.txt"
    ]

    while True:
        print("Available course files:")
        for file in available_files:
            print("-", file)

        filename = input("\nEnter course file: ").strip()

        if filename in available_files and os.path.exists(filename):
            return filename

        print("Invalid file. Please try again.\n")


# Select input file
filename = get_course_file()

files = [filename]


# Story 1: Get available courses
available_courses = get_all_available_courses(files)

print("\nAvailable courses:")
print(available_courses)


# Story 2: Get number of courses
max_n = len(available_courses)

n = get_course_count(max_n)

print(f"\nYou need to select {n} courses.")


# Keep asking until a valid schedule is found
while True:

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


    # Story 5: Generate final schedule
    if schedule is not None:
        print("\nFinal Schedule:")
        print(generate_schedule(schedule))
        break

    else:
        print("\nNo valid schedule can be created.")
        print("Please select your courses again.\n")