import error
import util
import parsers
import pretty
import printer
import sys


def usage(command: str) -> None:
    # print("Command: " + command)
    print("Usage: python main.py [option] source.py")
    print("   converts 'source.py' from mini-Python syntax to TypeScript syntax")
    print("   use option '--check' to ensure that two source files have the same AST")
    print("   use option '--parse' to display the AST of a source file")
    print("   use option '--regions' to display the same AST with regions")
    print("   use option '--pretty' to format a mini-Python source file")
    sys.exit(0)


def check(filename1: str, filename2: str) -> bool:
    # parse without regions
    p1 = parsers.parse_from_file(filename1)
    p2 = parsers.parse_from_file(filename2)
    return p1 == p2


def main(args: list[str]) -> None:
    match args:
        case [_, "--check", filename1, filename2]:
            if not check(filename1, filename2): error.prerr("Warning: AST mismatch.")
        case [_, "--parse", filename]:
            p = parsers.parse_from_file(filename)
            print(util.display(p))
        case [_, "--regions", filename]:
            p = parsers.parse_with_regions(filename)
            print(util.display(p))
        case [_, "--pretty", filename]:
            p = parsers.parse_with_regions(filename)
            print(pretty.str_of_prog(p))
        case [_, filename]:
            p = parsers.parse_with_regions(filename)
            print(printer.str_of_prog(p))
        case [command, *_]: usage(command)


main(sys.argv)
