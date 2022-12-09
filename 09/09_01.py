from enum import Enum
from functools import partial


class Direction(Enum):

    LEFT = partial(lambda i, j: (i, j - 1))
    UP = partial(lambda i, j: (i - 1, j))
    RIGHT = partial(lambda i, j: (i, j + 1))
    DOWN = partial(lambda i, j: (i + 1, j))

    @staticmethod
    def from_str(direction_str: str) -> "Direction":
        if direction_str == "L":
            return Direction.LEFT
        elif direction_str == "U":
            return Direction.UP
        elif direction_str == "R":
            return Direction.RIGHT
        elif direction_str == "D":
            return Direction.DOWN
        else:
            raise ValueError(f"{direction_str} is not a valid Direction string.")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        head_pos_acc, tail_pos_acc = [], []
        head_pos, tail_pos = (0, 0), (0, 0)
        for move in f.readlines():
            direction_str, num_steps = move.split(" ")
            direction = Direction.from_str(direction_str)
            num_steps = int(num_steps)
            for step in range(num_steps):
                head_pos = direction.value(*head_pos)
                diff = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
                abs_diff = abs(diff[0]), abs(diff[1])
                correction = max(min(diff[0], 1), -1), max(min(diff[1], 1), -1)
                if max(abs_diff) == 2:
                    tail_pos = tail_pos[0] + correction[0], tail_pos[1] + correction[1]
                head_pos_acc.append(head_pos)
                tail_pos_acc.append(tail_pos)
    print(head_pos, tail_pos)
    print(len(set(head_pos_acc)), len(set(tail_pos_acc)))
