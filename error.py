from typing import NoReturn

import sys

type region = tuple[int, int, int | None, int | None]

# Global variables
filename = "<string>"  # default name if no filename is available
regions = False  # True if the regions are stored in the AST
module = True  # True if the file contains a module

def to_string(r: region) -> str:
    (l1, c1, l2, c2) = r
    lines = str(l1) + ("" if l2 is None or l1 == l2 else "-" + str(l2))
    columns = str(c1 + 1) + ("" if c2 is None else "-" + str(c2 + 1))
    return "line " + lines + ", column " + columns


def prerr(msg: str) -> None:
    sys.stderr.write(msg + '\n')


def fail(r: region, err: Exception) -> NoReturn:
    prerr('File "' + filename + '", ' + to_string(r) + ":")
    prerr("  " + type(err).__name__ + ": " + str(err))
    sys.exit(1)


# error message syntax recognized by vscode:
# print('File "error.py", line 24, column 22:')
# print('File "error.py", line 24, column 22-30:')
# print('File "error.py", line 24-26, column 22-16:')
