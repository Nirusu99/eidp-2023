from result import Err, Ok, Panick, Result
from ui import run_command, Color
from spacearena import Difficulty, SpaceArena



if __name__ == '__main__':


if __name__ == '__main__':
    difficulty: Difficulty | None = None
    while not difficulty:
        difficulty = Difficulty.get_difficulty(
            input(f"Choose your difficulty {[e.name.lower() for e in list(Difficulty)]}\n> ").upper())
    print(f"Difficulty: {difficulty} selected!")
    game = SpaceArena(difficulty)
    print("Starting game!")
    while game.is_running:
        Err("error value hehe").unwrap_or("yay still works")
        match run_command(input("> "), game):
            case Ok(value):
                print(f"{Color.OK}{value}{Color.ENDC}")
            case Err(value):
                print(f"{Color.BOLD}{Color.FAIL}Error:{Color.ENDC} {Color.WARNING}{value}{Color.ENDC}")


