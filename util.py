from dataclasses import fields, is_dataclass


def newline(depth: int = 0, indent=" ") -> str:
    return "\n" + depth * indent


def is_structured(value: object) -> bool:
    return is_dataclass(value) or type(value) in [tuple, list]


def display_seq(values: list[object], depth: int, name: str = "", left: str = "(", right: str = ")") -> str:
    is_struct = any(is_structured(v) for v in values)
    return (newline(depth) + name + left +
            ", ".join(display(v, depth + 1) for v in values) +
            (newline(depth) if name == "" and is_struct else "") +
            right)


def display(value: object, depth: int = 0) -> str:
    if is_dataclass(value) and not isinstance(value, type):
        name = type(value).__name__
        values = [getattr(value, field.name) for field in fields(value)]
        return display_seq(values, depth, name)
    elif isinstance(value, tuple):
        return display_seq(list(value), depth)
    elif isinstance(value, list):
        return display_seq(value, depth, left="[", right="]")
    elif isinstance(value, str):
        return "'" + str(value) + "'"
    else:
        return str(value)
