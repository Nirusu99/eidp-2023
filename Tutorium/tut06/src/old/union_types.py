from dataclasses import dataclass
from typing import Callable

type Optional[T] = T | None


@dataclass
class FilteredList[E]:
    lst: list[E]
    filter: Callable[[E], bool]

    def __init__(self, filter=lambda _: True):
        self.lst = []
        self.filter = filter

    def append(self, item: E):
        if self.filter(item):
            self.lst += [item]

    def get(self, index: int) -> Optional[E]:
        if index < len(self.lst):
            return self.lst[index]

    def __str__(self) -> str:
        return str(self.lst)


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    filter_list = FilteredList(filter=is_even)
    filter_list.append(0)
    print(filter_list)
    filter_list.append(2)
    print(filter_list)
    filter_list.append(3)
    print(filter_list)
