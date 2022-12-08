import copy
from enum import Enum
from functools import partial


class Direction(Enum):

    LEFT = partial(lambda i, j: (i, j - 1))
    TOP = partial(lambda i, j: (i - 1, j))
    RIGHT = partial(lambda i, j: (i, j + 1))
    BOTTOM = partial(lambda i, j: (i + 1, j))


def count_score(i: int, j: int, dir: Direction, tree_map: list) -> int:
    score = 0
    init_tree = tree_map[i][j]
    while True:
        i, j = dir.value(i, j)
        if i < 0 or j < 0:
            return score
        try:
            next_tree = tree_map[i][j]
        except IndexError:
            return score
        score += 1
        if next_tree >= init_tree:
            return score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tree_map_str = f.read().strip("\n")
    tree_map = [list(row) for row in tree_map_str.split("\n")]
    score_map = copy.deepcopy(tree_map)
    height, width = len(tree_map), len(tree_map[0])
    best_tree = 0
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:
                score_map[i][j] = 0
                continue
            score = 1
            for dir in Direction:
                score *= count_score(i, j, dir, tree_map)
            score_map[i][j] = score
            if score > best_tree:
                best_tree = score
    print(best_tree)
