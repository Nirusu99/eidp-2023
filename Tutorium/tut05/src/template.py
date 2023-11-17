from dataclasses import dataclass


# the greatest common divisor of two numbers `a`, `b`
def gcd(a, b):
    pass


# this shortens a fraction to its most reduced representation
def shorten_fraction(fraction):
    pass


@dataclass
class Fraction:

    # Multiplication of two fractions
    # `Fraction(1 / 2) * Fraction(2 / 6) -> Fraction(1, 6)`
    # Extra: make it possible to multiply `int` with a fraction
    # `Fraction(1 / 2) * 2 -> Fraction(1 / 4)`
    def __mul__(self, o):
        pass

    # The division of two fraction
    # `Fraction(1 / 2) / Fraction(2 / 6) -> Fraction(3, 2)`
    # Extra: make it possible to divide `int` with a fraction
    # `Fraction(1 / 4) / 2 -> Fraction(1 / 2)`

    def __truediv__(self, o):
        pass

    # The negative of a fraction
    # `-Fraction(1 / 2) -> Fraction(-1 / 2)`

    def __neg__(self):
        pass

    # The addition of two fractions
    # `Fraction(1 / 4) + Fraction(2 / 8) -> Fraction(1 / 2)`
    # Extra: make it possible to add `int` with a fraction
    # `Fraction(1 / 4) + 1 -> Fraction(5 / 4)`

    def __add__(self, o):
        pass

    # The subtraction of two fractions
    # `Fraction(1 / 2) - Fraction(1 / 4) -> Fraction(1 / 4)`
    # Extra: make it possible to subtract `int` with a fraction
    # `Fraction(5 / 2) - 1 -> Fraction(3 / 2)`

    def __sub__(self, o):
        pass

    # The `equal`-function is == and should only care about reduced fractions
    # `Fraction(1 / 2) == Fraction(2 / 4)` is True

    def __eq__(self, o):
        pass

    # The `not equal`-function is != and should only care about reduced fractions exactly as equal

    def __neq__(self, o):
        pass

    # The str function should return this string `(divident / divisor)`

    def __str__(self):
        pass
