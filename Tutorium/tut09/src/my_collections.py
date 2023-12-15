from dataclasses import dataclass, InitVar


@dataclass
class MyList[T]:
    internal_list: InitVar[list[T]]
    length: InitVar[int]
    
    def __init__(self):
        self.__internal_list = []
        self.__length = 0
        
    def add(self, item: T):
        self.__internal_list += [item]
        self.__length += 1
        

    @property
    def length(self) -> int:
        return self.__length

@dataclass
class GameObject:
    position: InitVar[tuple[int, int]]

    def __post_init__(self, position: tuple[int, int]):
        assert (0, 0) <= position
        self.__position = position

    @property
    def position(self) -> tuple[int, int]:
        return self.__position

    @position.setter
    def position(self, position: tuple[int, int]):
        if (0, 0) > position:
            return
        self.__position = position
    
if __name__ == "__main__":
    xs: MyList[int] = MyList()
    xs.add(100)
    assert xs.length == 1
    position = (0, 0)
    my_obj = GameObject(position)
    assert my_obj.position == (0, 0)
    try:
        GameObject((0, -1))
    except AssertionError:
        pass
    else:
        raise AssertionError(f"{my_obj} should have thrown a assertation error")
    my_obj.position = (-1, 0)
    assert my_obj.position == (0, 0)
    