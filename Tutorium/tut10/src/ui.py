from abc import ABC, abstractmethod
from enum import Enum 
import re
from typing import override
from result import Ok, Err, Result
from spacearena import Difficulty, SpaceArena

class Color(Enum):
    OK = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    def __str__(self) -> str:
        return self.value
    

class AbstractCommand(ABC):
   
    def matches(self, inp: str) -> Result[re.Match[str], None]:
        if m := re.match(self.pattern(), inp):
            return Ok(m)
        return Err(None)
    
    @abstractmethod
    def pattern(self) -> str:
        pass
    
    @abstractmethod
    def run(self, game: SpaceArena, args: list[str]) -> Result[str, str]:
        pass
    
    
class QuitCommand(AbstractCommand):
    @override
    def pattern(self) -> str:
        return r"(quit)"
    
    @override
    def run(self, game: SpaceArena, _: list[str]) -> Result[str, str]:
        game.stop()
        return Ok('quitting game!')
    
class DifficultyCommand(AbstractCommand):
    @override
    def pattern(self) -> str:
        return r"(difficulty|diff)\s+(increase|decrease)"
    
    @override
    def run(self, game: SpaceArena, args: list[str]) -> Result[str, str]:
        diffs = list(Difficulty)
        curr = diffs.index(game.difficulty)
        
        match args[0]:
            case 'increase' if curr + 1 < len(diffs):
                game.difficulty = diffs[curr + 1]
                return Ok(f"Increasing difficulty to {game.difficulty}")
            case 'increase':
                return Err("maximum difficulty")
            case 'decrease' if curr - 1 >= 0:
                game.difficulty = diffs[curr - 1]
                return Ok(f"Decreasing difficulty to {game.difficulty}")
            case 'decrease':
                return Err("minimum difficulty")
        return Err("invalid input")
    
ALL_COMMANDS: list[AbstractCommand] = [QuitCommand(), DifficultyCommand()]
    
def run_command(inp: str, game: SpaceArena, commands: list[AbstractCommand] = ALL_COMMANDS) -> Result[str, str]:
    for command in commands:
        match command.matches(inp):
            case Ok(value):
                args = [str(s) for s in value.groups()]
                return command.run(game, args[1:])
        
    
    return Err("command not found")