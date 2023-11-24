from dataclasses import dataclass


@dataclass
class Element[T]:
    value: T
    next: 'Element[T] | None'


@dataclass
class MyList[T]:
    head: Element[T] | None = None
    last: Element[T] | None = None
    length: int = 0

    def push_back(self, value: T):
        if not self.head:
            self.head = Element(value, None)
            self.last = self.head
            self.length += 1
            return

        self.last.next = Element(value, None)
        self.last = self.last.next
        self.length += 1

    def remove(self, index: int) -> T | None:
        if self.length <= index:
            return

        if index == 0:
            self.head = self.head.next
            self.last = self.head
            self.length -= 1

        i = index
        previous = self.head
        current = self.head
        while current and i > 0:
            previous = current
            current = current.next
            i -= 1

        if i != 0 or not current:
            return
        if not current.next:
            self.last = previous
        previous.next = current.next
        self.length -= 1
        return current.value

    def __str__(self) -> str:
        output = ""
        current = self.head
        while current:
            output += str(current.value)
            if current.next:
                output += ", "
            current = current.next
        return f"[{output}]"

    def __getitem__(self, index: int) -> T | None:
        if self.length <= index:
            return

        current = self.head
        i = index

        while current and i > 0:
            current = current.next
            i -= 1

        if i == 0 and current:
            return current.value

    def __setitem__(self, index: int, new_value: T):
        if self.length <= index:
            return

        current = self.head
        i = index

        while current and i > 0:
            current = current.next
            i -= 1

        if i == 0 and current:
            current.value = new_value

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> 'MyList.Iter[T]':
        return MyList.Iter(self.head)

    @dataclass
    class Iter[E]:
        current: Element[E]

        def __next__(self) -> E:
            if not self.current:
                raise StopIteration
            val = self.current.value
            self.current = self.current.next
            return val


if __name__ == "__main__":
    lst: MyList[int] = MyList()
    lst.push_back(0)
    lst.push_back(3)
    lst.push_back(2)
    assert lst[0] == 0 and lst[1] == 3 and lst[2] == 2
    print(lst)
    lst.remove(1)
    assert lst[0] == 0 and lst[1] == 2
    print(lst)
    lst[1] = 3
    assert lst[0] == 0 and lst[1] == 3 and len(lst) == 2
    print(lst)
    assert lst.remove(1)
    assert lst.last.value == 0
    lst.remove(0)
    assert len(lst) == 0
    assert not lst.head
    assert not lst.last

    for i in range(0, 10):
        lst.push_back(i)
    for it in lst:
        print(it)
