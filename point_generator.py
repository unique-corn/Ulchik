from random import randint
from typing import List, Generator, Tuple


def point_generator(num: int, range_: (int, int)=(-228, 228)) -> Generator[Tuple[int, int], None, None]:
    for _ in range(num):
        yield randint(*range_), randint(*range_)


def generate_points(num: int, range_: (int, int)=(-228, 228)) -> List[Tuple[int, int]]:
    X, Y = [], []

    for x, y in point_generator(num, range_):
        X.append(x)
        Y.append(y)

    return X, Y
