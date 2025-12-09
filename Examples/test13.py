from dataclasses import dataclass


@dataclass
class Point: x: int; y: int


pt: Point = Point(x=3, y=5)


def init(z: int) -> Point:
    return Point(x=z, y=z)


print(pt.y)
