from typing import Any, Callable, Iterable, Iterator
    

def map[T, R](func: Callable[[T], R], xs: Iterable[T]) -> Iterable[R]:
    return [func(x) for x in xs]


def filter[T](predicate: Callable[[T], bool], xs: Iterable[T]) -> Iterable[T]:
    return [x for x in xs if predicate(x)]


def fold[T](func: Callable[[T, T], T], xs: Iterable[T]) -> T:
    it: Iterator[T] = iter(xs)
    value: T | None = None
    for x in it:
        match value:
            case None:
                value = x
            case _:
                value = func(value, x)
    if not value:
        raise TypeError("can't fold empty list")
    return value

def flatten(xs: Iterable[Any]) -> Iterable[Any]:
    new_list = []
    for s in xs:
        if isinstance(s, Iterable):
            new_list += flatten(s)
        else:
            new_list.append(s)
    return new_list

def compose[T](*funcs: Callable[[T], T]) -> Callable[[T], T]:
    return fold(lambda f, g: lambda n: f(g(n)), funcs)


def poly(x: float) -> Callable[[float, float], Callable[[float], float]]:
    return lambda a, b: lambda c: a * x ** 2 + b * x + c

def main():
    f: Callable[[int], int] = lambda n: n + 42
    g: Callable[[int], int] = lambda n: n ** 2
    h: Callable[[int], int] = lambda n: n - 3

    fhg: Callable[[int], int] = compose(f, g, h)

    # f(g(h(0))) <=> ((0 - 3) ** 2) + 42 = 51
    assert (tmp := fhg(0)) == 51
    assert compose(f, g, h)(0) == 51
    predicate = lambda e: e
    assert list(filter(predicate, [1, 2, 3, None, 5, 6])) == [1, 2, 3, 5, 6]
    assert list(filter(lambda e: e is None, [1, 2, 3, None, 5, 6])) == [None]

    assert list(map(lambda e: str(e), [1, 2, 3, 4, 5, 6, "hello_functional"])) == ["1", "2", "3", "4", "5", "6", "hello_functional"]
    
    assert list(
        filter(lambda e: len(e) > 1,
               map(lambda e: str(e),
                   [1, 2, 3, 4, "hello_world"]))) == ["hello_world"]

    assert list(filter(lambda e: isinstance(e, int), [1, 2, 3, "hello"])) == [1, 2, 3]
    assert (tmp := list(flatten([[1, 2, 3], 4, [[5, 6], 7, [8, 9]]]))) == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"{tmp}"

    def add(a: int, b: int) -> int:
        return a + b

    add_but_variable: Callable[[int, int], int] = add
    
    assert add_but_variable(3, 2) == 5
    
    add2: Callable[[int, int], int] = lambda x, y: x + y
    
    assert add2(2, 3) == 5
    
    assert (lambda x, y: x + y)(3, 4) == 7
    
    sum: Callable[[Iterable[int]], int] = lambda xs: fold(lambda x, y: x + y, xs)
    assert sum([1, 2, 3, 4]) == 10
    
    assert poly(3)(2, 3)(5) == 2 * 3 ** 2 + 3 * 3 + 5

if __name__ == '__main__':
    main()