from union_types import FilteredList, is_even


class PrintableInt(int):
    def print(self):
        print(self)


if __name__ == "__main__":
    lst: FilteredList[PrintableInt] = FilteredList(filter=is_even)
    lst.append(PrintableInt(0))
    lst.get(0).print()
    match lst.get(1):
        case None:
            pass
        case PrintableInt(n):
            n.print()

    lst.append(PrintableInt(2))
    lst.get(1).print()
