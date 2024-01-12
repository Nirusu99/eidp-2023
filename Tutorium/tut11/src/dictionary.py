from dataclasses import InitVar, dataclass
from typing import Any, Callable


def iterating_dict():
    courses: dict[str, list[str]] = {
        "eidp": ["np19", "az34", "jf334"],
        "mathe": ["aw331", "pl67"],
        "sdp": ["xy111", "xz112"],
    }
    
    for course, students in courses.items():
        print(f"{courses}: {students}")

def mutable_keys():
    lists_as_keys: dict[list[str], str] = {
        ["np19", "az34", "jf334"]: "eidp",  # type: ignore
        ["aw331", "pl67"]: "mathe",         # type: ignore
        ["xy111", "xz112"]: "sdp",          # type: ignore
    }
    print(lists_as_keys)
    
def what_is_a_value():
    ops: dict[str, Callable] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

can_execute = True
def function(x: int) -> int:
    global can_execute
    if can_execute:
        can_execute = False
        return x + 1
    return x

def can_execute_again():
    global can_execute
    can_execute = True
    
@dataclass
class Point:
    def __post_init__(self):
        self.__x = 0
        self.__y = 0
    
    @property
    def x(self) -> float:
        return self.__x