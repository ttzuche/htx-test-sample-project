def add(a: float, b: float) -> float:
    return a + b


def negate(a: float) -> float:
    return -a


def absolute(a: float) -> float:
    return abs(a)


def square(a: float) -> float:
    return a * a


def double(a: float) -> float:
    return a * 2


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    return a**b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
