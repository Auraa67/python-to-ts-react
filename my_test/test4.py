from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int
type Shape = Rectangle

def get_area(s: Shape) -> int:
    match s:
        case Rectangle(width=w, height=h):
            return w * h
        case _:
            return 0

r = Rectangle(width=10, height=5)

print(get_area(r))