from .calculator import (
    absolute,
    add,
    divide,
    double,
    half,
    modulo,
    multiply,
    negate,
    power,
    square,
    subtract,
    triple,
)


def main() -> None:
    """Print demo calculator results for supported operations.

    Inputs:
        None.

    Outputs:
        None. Writes formatted example calculations to stdout.
    """
    print("Sample calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"17 % 5 = {modulo(17, 5)}")
    print(f"-(7) = {negate(7)}")
    print(f"|-9| = {absolute(-9)}")
    print(f"5² = {square(5)}")
    print(f"6 x2 = {double(6)}")
    print(f"4 x3 = {triple(4)}")
    print(f"10 /2 = {half(10)}")


if __name__ == "__main__":
    main()
