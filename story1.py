def extract_course_numbers(lines):
    """
    Extract unique course numbers from file lines.
    Args:
        lines (list[str]): input file lines
    Returns:
        list[str]: sorted unique course numbers
    """
    course_set = set()

    for line in lines:
        parts = line.strip().split()

        if len(parts) == 0:
            continue

        course_set.add(parts[0])

    return sorted(course_set)


def read_file(filename):
    """
    Read a file and return lines.
    Args:
        filename (str)
    Returns:
        list[str]
    """
    with open(filename, "r") as f:
        return f.readlines()


def get_all_available_courses(files):
    """
    Read multiple files and return all unique course numbers.
    Args:
        files (list[str])
    Returns:
        list[str]
    """
    all_lines = []

    for file in files:
        all_lines.extend(read_file(file))

    return extract_course_numbers(all_lines)

