from dataclasses import dataclass

@dataclass
class Red:
    pass

@dataclass
class Blue:
    pass

@dataclass
class Green:
    pass

type Color = Red | Blue | Green

def is_red(c: Color) -> int:
    match c:
        case Red():
            return 1
        case Blue():
            return 0
        case Green():
            return 0
        case _:
            return 0
        
print(is_red(Red()))