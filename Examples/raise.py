def f() -> str:
    # raise TypeError
    # raise TypeError()
    raise TypeError("error message")


def main() -> str:
    try:
        return f()
    except TypeError as err:
        return "Type error: " + str(err)


print(main())
