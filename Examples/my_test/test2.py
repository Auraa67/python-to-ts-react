from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def sum_x_coords(points: list[Point]) -> int:
    match points:
        case [head, *tail]:
            match head:
                case Point(x=val, y=_):
                    return val + sum_x_coords(tail)
                case _:
                    return sum_x_coords(tail)
        case _:
            return 0

my_path: list[Point] = [Point(x=1, y=1), Point(x=10, y=5), Point(x=100, y=50)]
print(sum_x_coords(my_path))