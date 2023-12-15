from dataclasses import dataclass

@dataclass
class A:
    x: int
    y: int = 0

    # die init die von `dataclass` generiert wird, also unnötig
    # siehe class B
    def __init__(self, x: int, y: int = 0):
        self.x = x
        self.y = y
        
@dataclass
class B:
    x: int
    y: int = 0
   
if __name__ == '__main__':
    my_a = A(1)
    assert my_a.x == 1
    assert my_a.y == 0
    my_other_a = A(1, y = 1)
    assert my_other_a.x == 1
    assert my_other_a.y == 1
    my_b = B(1)
    assert my_b.x == 1
    assert my_b.y == 0
    my_other_b = B(1, y = 1)
    assert my_other_b.x == 1
    assert my_other_b.y == 1