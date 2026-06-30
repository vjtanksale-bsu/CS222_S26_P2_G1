from story1 import get_all_available_courses
from story2 import get_course_count
from story3 import select_courses

# input files
files = ["courses.txt", "courses1.txt", "courses2.txt"]

# Step 1: get available courses from story1
available_courses = get_all_available_courses(files)
print("Available courses:", available_courses)

# Step 2: get number of courses from story2
max_n = len(available_courses)
n = get_course_count(max_n)

print(f"\nYou need to select {n} courses.")

# Step 3: select courses from story3
selected_courses = select_courses(n, available_courses)

# Final output
print("\nSelected courses:", selected_courses)