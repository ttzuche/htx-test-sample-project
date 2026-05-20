from .calculator import absolute, add, divide, modulo, multiply, negate, power, subtract


def main() -> None:
    print("Sample calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"17 % 5 = {modulo(17, 5)}")
    print(f"-(7) = {negate(7)}")
    print(f"|-9| = {absolute(-9)}")


if __name__ == "__main__":
    main()
