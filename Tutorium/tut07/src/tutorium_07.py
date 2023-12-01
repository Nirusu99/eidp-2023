def fibonacci(n: int) -> int:
    if n in {0, 1}:  # Abbruchbedingung
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # mehrere Rekursionsaufrufe


def fac(n: int) -> int:
    if n <= 0:  # Abbruchbedingung, kein Rekursiver Aufruf mehr!
        return 1
    return n * fac(n - 1)  # Rekursiver Aufruf


def fac2(n: int) -> int:
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def ack(n: int, m: int) -> int:
    match (n, m):
        case (0, _):
            return m + 1
        case (_, 0):
            return ack(n - 1, 1)
        case _:
            return ack(n - 1, ack(n, m - 1))


def all_fac(max: int) -> list[tuple[int, int]]:
    if max == 0:  # Abbruchbedingung
        return [(0, 1)]
    return [(max, fac(max))] + all_fac(max - 1)  # Rekursion


def all_fac_str(min: int, max: int) -> str:
    if min >= max:  # Abbruchbedingung
        return f"{fac(min)}"
    return f"{fac(min)} " + all_fac_str(min + 1, max)  # Rekursion


def fib_str(n: int) -> str:
    if n in {0, 1}:
        return str(n)
    return f"({fib_str(n - 1)} + {fib_str(n - 2)})"


if __name__ == "__main__":
    assert [fibonacci(n) for n in range(15)] == [0, 1, 1, 2,
                                                 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert [fac(n) for n in range(11)] == [1, 1, 2, 6, 24,
                                           120, 720, 5040, 40320, 362880, 3628800]
    assert [fac(n) for n in range(10)] == [fac2(n) for n in range(10)]
    assert list(reversed(all_fac(10))) == [(n, fac(n)) for n in range(11)]
    assert all_fac_str(0, 10) == "1 1 2 6 24 120 720 5040 40320 362880 3628800"
