from dataclasses import dataclass, InitVar
from enum import Enum
from typing import Optional


class Difficulty(Enum):
    EASY    = 0.5
    NORMAL  = 1.0
    HARD    = 2.0
   
    @staticmethod
    def get_difficulty(input: str) -> Optional['Difficulty']:
        for e in list(Difficulty):
            if e.name == input:
                return e
            
    def __str__(self):
        return self.name
            


@dataclass
class SpaceArena:
    _difficulty: InitVar[Difficulty] = Difficulty.NORMAL
    
    def __post_init__(self, difficulty: Difficulty = Difficulty.NORMAL) -> None:
        self.__difficulty = difficulty
        self.__is_running = True
        
        
    @property
    def difficulty(self) -> Difficulty:
        return self.__difficulty
    
    @difficulty.setter
    def difficulty(self, new_diff: Difficulty):
        self.__difficulty = new_diff
    
    @property
    def is_running(self) -> bool:
        return self.__is_running
    
    def stop(self):
        self.__is_running = False