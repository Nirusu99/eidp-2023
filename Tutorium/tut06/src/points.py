from dataclasses import dataclass


@dataclass
class Point1D[T]:
    x: T


@dataclass
class Point2D[T]:
    x: T
    y: T


@dataclass
class Point3D[T]:
    x: T
    y: T
    z: T


type Point[T] = Point1D[T] | Point2D[T] | Point3D[T]


def print_point[T](pt: Point[T]) -> None:
    match pt:
        case Point1D(0) | Point2D(0, 0) | Point3D(0, 0, 0):
            print("Nullpunkt!")
        case Point1D(x):
            print(f"Point1D: ({x})")
        case Point2D(x, y):
            print(f"Point2D: ({x}, {y})")
        case Point3D(x, y, z):
            print(f"Point3D: ({x}, {y}, {z})")
        case _:
            print("Not a point!")


def match_list(some_list: list[str]) -> None:
    match some_list:
        case ["🤡", *other]:
            print(f"your list starts with 🤡 and the rest is {other}")
        case _:
            print("your list doesn't start with 🤡")


if __name__ == "__main__":
    print_point(Point1D(1))  # (1)
    print_point(Point2D(1, 2))  # (1, 2)
    print_point(Point3D(1, 2, 3))  # (1, 2, 3)
    print_point(Point3D(0, 0, 0))  # (1, 2, 3)
    print_point("not a point")  # Not a point!
    match_list(["🤡", "ich", "hasse", "python", "manchmal"])
