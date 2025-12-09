def count_passed(grades: list[int]) -> int:
    match grades:
        case [g, *rest]:
            if g >= 10:
                return 1 + count_passed(rest)
            else:
                return count_passed(rest)
        case _:
            return 0

class_grades = [12, 8, 15, 5, 10]

print(count_passed(class_grades))