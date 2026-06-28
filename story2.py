def is_valid_course_count(value):
    """
    Validate whether input is a valid course count.
    Must be integer between 1 and 7.
    """

    try:
        number = int(value)
        return 1 <= number <= 7
    except (ValueError, TypeError):
        return False


def parse_course_count(value):
    """
    Convert valid input to integer.
    Assumes validation already passed.
    """
    return int(value)


def get_course_count():
    """
    Interactive loop: keeps asking until valid input is entered.
    """

    while True:
        user_input = input("Enter number of courses (1-7): ")

        if is_valid_course_count(user_input):
            return parse_course_count(user_input)

        print("Invalid input. Please enter an integer between 1 and 7.")


if __name__ == "__main__":
    n = get_course_count()
    print("You selected:", n)