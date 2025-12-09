from dataclasses import dataclass, replace
@dataclass
class Point:
    x: int
    y: int
pt: Point = Point(x=3, y=5)
def init(z: int) -> Point:
    return Point(x=z, y=z)
pt2: Point = replace(pt, y=10)

print(pt2)
