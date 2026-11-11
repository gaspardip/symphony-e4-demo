"""Small arithmetic helpers used by the Symphony E4 demo."""


def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def clamp(value: int, low: int, high: int) -> int:
    if low > high:
        raise ValueError("low must be less than or equal to high")
    if value < low:
        return low
    if value > high:
        return high
    return value
