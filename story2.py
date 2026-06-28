def is_valid_course_count(value):
    """
    Validate whether input is a valid course count.
    Clean logic function (TDD-friendly).
    """

    try:
        number = int(value)
        return number > 0
    except (ValueError, TypeError):
        return False


def parse_course_count(value):
    """
    Convert valid input to integer.
    Assume validation already passed.
    """
    return int(value)


def get_course_count():
    """
    Interactive function (user input loop).
    Keeps asking until valid input is entered.
    """

    while True:
        user_input = input("Enter number of courses: ")

        if is_valid_course_count(user_input):
            return parse_course_count(user_input)

        print("Invalid input. Please enter an integer > 0.")

if __name__ == "__main__":
    n = get_course_count()
    print("You selected:", n)