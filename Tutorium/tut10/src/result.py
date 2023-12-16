from abc import ABC
from dataclasses import dataclass
from typing import Callable, overload

class Panick(Exception):
    def __init__(self, msg_res: 'Err | str') -> None:
        match msg_res:
            case str(msg):
                super().__init__(msg)
            case _: 
                super().__init__(f"thread `__main__` panicked:\ncalled `Result::unwrap()` on an `Err` value: \"{msg_res.value}\"")
        
    
@dataclass
class Result[V, E](ABC):
    def unwrap(self) -> V:
        match self:
            case Ok(value):
                return value
        raise Panick(self) # type: ignore
    
    def expect(self, msg: str) -> V:
        match self:
            case Ok(value):
                return value
        raise Panick(msg)
    
    def is_ok(self) -> bool:
        return isinstance(self, Ok)
    
    def is_err(self) -> bool:
        return isinstance(self, Err)
    
    def unwrap_or(self, value: V) -> V:
        match self:
            case Ok(val):
                return val
        return value
    
    def and_[O](self, other: 'Result[O, E]') -> 'Result[O, E]':
        match self, other:
            case Err(value), _:
                return Err(value)
        return other
    
    def and_then[O](self, func: Callable[[V], 'Result[O, E]']) -> 'Result[O, E]':
        match self:
            case Ok(value):
                return func(value)
        return Err(self.value) # type: ignore

@dataclass    
class Ok[V, E](Result[V, E]):
    value: V

@dataclass
class Err[V, E](Result[V, E]):
    value: E
    
def __sqrt(num: float) -> Result[float, str]:
    if num < 0:
        return Err('negative sqrt')
    return Ok(num ** 0.5)

def test_result() -> None:
    assert Ok(4.0).and_then(__sqrt) == Ok(2.0)
    assert Ok(-5.0).and_then(__sqrt) == Err('negative sqrt')
    assert Err("haha error").and_then(__sqrt) == Err("haha error")
    assert Ok("test").unwrap() == "test"
    try:
        Err("haha error").unwrap()
    except Panick:
        pass
    else:
        assert False, 'didn\'t throw Panick'
    assert Err('haha error').unwrap_or("doch nicht") == 'doch nicht'
    
    result = Ok('test result')
    
    match result:
        case Ok(res):
            assert res == 'test result'
        case Err():
            pass
        
    result = Err('test result')
    
    match result:
        case Ok():
            pass
        case Err(res):
            assert res == 'test result'