def add_mark(student_marks, name, mark):
    student_marks[name] = mark
    return student_marks


def update_mark(student_marks, name, new_mark):
    if name in student_marks:
        student_marks[name] = new_mark
        return True
    return False


def delete_mark(student_marks, name):
    if name in student_marks:
        del student_marks[name]
        return True
    return False


def calculate_average(student_marks):
    if not student_marks:
        return 0
    return sum(student_marks.values()) / len(student_marks)


def highest_mark(student_marks):
    if not student_marks:
        return None, None
    name = max(student_marks, key=student_marks.get)
    return name, student_marks[name]


def lowest_mark(student_marks):
    if not student_marks:
        return None, None
    name = min(student_marks, key=student_marks.get)
    return name, student_marks[name]
