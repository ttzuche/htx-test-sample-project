from .calculator import add, divide, multiply, subtract


def main() -> None:
    print("Sample calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")


if __name__ == "__main__":
    main()
