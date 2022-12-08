import copy
from enum import Enum
from functools import partial


class Direction(Enum):

    LEFT = partial(lambda i, j: (i, j - 1))
    TOP = partial(lambda i, j: (i - 1, j))
    RIGHT = partial(lambda i, j: (i, j + 1))
    BOTTOM = partial(lambda i, j: (i + 1, j))


def find_is_visible(i: int, j: int, dir: Direction, tree_map: list) -> bool:
    init_tree = tree_map[i][j]
    while True:
        i, j = dir.value(i, j)
        if i < 0 or j < 0:
            return True
        try:
            next_tree = tree_map[i][j]
        except IndexError:
            return True
        if next_tree >= init_tree:
            return False


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tree_map_str = f.read().strip("\n")
    tree_map = [list(row) for row in tree_map_str.split("\n")]
    visible_map = copy.deepcopy(tree_map)
    height, width = len(tree_map), len(tree_map[0])
    tree_count = 0
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0:
                visible_map[i][j] = True
                tree_count += 1
                continue
            visible = False
            for dir in Direction:
                if find_is_visible(i, j, dir, tree_map):
                    visible = True
                    tree_count += 1
                    break
            visible_map[i][j] = visible
    print("\n".join(["".join(["T" if i else "_" for i in row]) for row in visible_map]))
    print(tree_count)
