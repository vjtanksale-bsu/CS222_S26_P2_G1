def is_valid_course_count(value, max_n):
    """Check if input is between 1 and max_n."""
    try:
        return 1 <= int(value) <= max_n
    except (ValueError, TypeError):
        return False


def parse_course_count(value):
    """Convert input to int."""
    return int(value)


def get_course_count(max_n):
    """Get valid course count from user."""
    while True:
        user_input = input(f"Enter number of courses (1-{max_n}): ")

        if is_valid_course_count(user_input, max_n):
            return parse_course_count(user_input)

        print("Invalid input.")