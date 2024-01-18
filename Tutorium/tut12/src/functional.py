from typing import Callable, Iterable, Iterator

type Optional[T] = T | None


def map[T, R](func: Callable[[T], R], xs: Iterable[T]) -> Iterable[R]:
    return [func(x) for x in xs]


def filter[T](func: Callable[[T], bool], xs: Iterable[T]) -> Iterable[T]:
    return [x for x in xs if func(x)]


def reduce[T](func: Callable[[T, T], T], xs: Iterable[T]) -> T:
    it: Iterator[T] = iter(xs)
    value: T
    try:
        x: T = next(it)
    except StopIteration:
        raise TypeError("can't reduce empty list")
    else:
        value = x
    for y in it:
        value = func(value, y)
    return value


def compose[T](*funcs: Callable[[T], T]) -> Callable[[T], T]:
    return reduce(lambda f, g: lambda n: f(g(n)), funcs)


f: Callable[[int], int] = lambda n: n + 42
g: Callable[[int], int] = lambda n: n ** 2
h: Callable[[int], int] = lambda n: n - 3

print(compose(f, g, h)(0))

print(list(filter(lambda e: bool(e), [1, 2, 3, None, 5, 6])))
print(list(filter(lambda e: not bool(e), [1, 2, 3, None, 5, 6])))

print(list(map(lambda e: str(e), [1, 2, 3, 4, 5, 6, "hello_functional"])))

print(list(
    filter(lambda e: len(e) > 1,
           map(lambda e: str(e),
               [1, 2, 3, 4, "hello_world"]))))

print(list(filter(lambda e: isinstance(e, int), [1, 2, 3, "hello"])))
