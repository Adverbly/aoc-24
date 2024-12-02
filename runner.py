import sys
import time
from importlib import import_module
import os

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"


def get_solution(day, part):
    """
    Dynamically import and return the solve module for a specific day and part.
    """
    try:
        module = import_module(f"solutions.day_{day}.part_{part}.solve")
        return module
    except ModuleNotFoundError:
        raise ValueError(f"Solution for day {day}, part {part} not found.")


def read_input(day, part, example):
    path = (
        f"solutions/day_{day}/part_{part}/{example}"
        if example
        else f"solutions/day_{day}/input.txt"
    )

    with open(path) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    data = sys.argv[1:]
    if len(data) == 3:
        day, part, example = data
    else:
        day, part = data
        example = None

    input = read_input(day, part, example)

    solution = get_solution(day, part)

    start = time.time()
    result = solution.run(input)
    end = time.time()

    print(f"Day {day} Part {part} result: {result} duration: {end - start}")
