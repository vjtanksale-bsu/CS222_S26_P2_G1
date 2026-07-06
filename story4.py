def parse_course(course_line):
    parts = course_line.split()
    return {
        "days": parts[2],
        "start": int(parts[3]),
        "end": int(parts[4])
    }

def has_time_conflict(selected_courses):
    course_info = {}
    for filename in ["courses.txt", "courses1.txt", "courses2.txt"]:
        try:
            with open(filename, "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.split()
                        course_id = parts[0]
                        course_info[course_id] = parse_course(line)
        except FileNotFoundError:
            continue

   
    for i in range(len(selected_courses)):
        for j in range(i + 1, len(selected_courses)):
            c1 = course_info.get(selected_courses[i])
            c2 = course_info.get(selected_courses[j])
            
            if c1 and c2:
                same_days = set(c1["days"]) & set(c2["days"])
                if same_days:
                    if max(c1["start"], c2["start"]) < min(c1["end"], c2["end"]):
                        return True  # Found a conflict!
                        
    return False 