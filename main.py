from story1 import get_all_available_courses
from story2 import get_course_count

files = ["courses.txt", "courses1.txt", "courses2.txt"]

available_courses = get_all_available_courses(files)

print("Available courses:", available_courses)

max_n = len(available_courses)

n = get_course_count(max_n)

print("You selected:", n)