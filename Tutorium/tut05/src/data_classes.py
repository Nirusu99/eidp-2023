from dataclasses import dataclass


def gcd(a: int, b: int) -> int:
    x = abs(a)
    y = abs(b)
    while (y):
        x, y = y, x % y
    return x


def shorten_fraction(fraction: 'Fraction') -> 'Fraction':
    g: int = gcd(fraction.divident, fraction.divisor)
    return Fraction(fraction.divident // g, fraction.divisor // g)


@dataclass
class Fraction:
    divident: int
    divisor: int

    def __neg__(self: 'Fraction') -> 'Fraction':
        return -1 * self

    def __mul__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        if isinstance(o, int):
            o = Fraction(o, 1)
        return shorten_fraction(Fraction(self.divident * o.divident,
                                         self.divisor * self.divisor))

    def __rmul__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        return self * o

    def __truediv__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        if isinstance(o, int):
            o = Fraction(o, 1)
        return shorten_fraction(Fraction(self.divident * o.divisor,
                                         self.divisor * o.divident))

    def __rtruediv___(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        return self / o

    def __add__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        if isinstance(o, int):
            o = Fraction(o, 1)
        g: int = gcd(self.divisor, o.divisor)
        l: int = abs(self.divisor * o.divisor) // g
        return shorten_fraction(Fraction(self.divident
                                         * (l // self.divisor)
                                         + o.divident
                                         * (l // o.divisor), l))

    def __radd__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        return self + o

    def __sub__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        if isinstance(o, int):
            o = Fraction(o, 1)
        return self + -o

    def __rsub__(self: 'Fraction', o: 'Fraction | int') -> 'Fraction':
        return self - o

    def __eq__(self: 'Fraction', o: 'Fraction | int') -> bool:
        if isinstance(o, int):
            o = Fraction(o, 1)
        shorten_self: 'Fraction' = shorten_fraction(self)
        shorten_o: 'Fraction' = shorten_fraction(o)
        return (shorten_self.divident == shorten_o.divident
                and shorten_self.divisor == shorten_o.divisor)

    def __neq__(self: 'Fraction', o: 'Fraction | int') -> bool:
        return not (self == o)

    def __str__(self: 'Fraction'):
        return f"({self.divident} / {self.divisor})"


if __name__ == "__main__":
    assert Fraction(1, 1) == 1
    assert Fraction(1, 2) == (out := Fraction(2, 4) /
                              Fraction(g := gcd(2, 4), g)), f"!= {out}"
    assert (sol := Fraction(9, 20)) == (
        res := Fraction(1, 5) + Fraction(1, 4)), f"!= {out}"
    assert (sol := Fraction(-9, 20)) == (
        res := Fraction(1, -5) + Fraction(-1, 4)), f"!= {out}"
    assert (sol := Fraction(-1, 20)) == (
        res := Fraction(1, 5) + Fraction(-1, 4)), f"!= {out}"
