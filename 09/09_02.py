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
        num_knots = 10
        head_pos_acc, tail_pos_acc = [], []
        knots = [(0, 0) for _ in range(num_knots)]
        i = 0
        for move in f.readlines():
            direction_str, num_steps = move.split(" ")
            direction = Direction.from_str(direction_str)
            num_steps = int(num_steps)
            for step in range(num_steps):
                knots[0] = direction.value(*knots[0])
                for knot_id in range(1, num_knots):
                    head_idx, tail_idx = knot_id - 1, knot_id
                    diff = (
                        knots[head_idx][0] - knots[tail_idx][0],
                        knots[head_idx][1] - knots[tail_idx][1],
                    )
                    abs_diff = abs(diff[0]), abs(diff[1])
                    correction = max(min(diff[0], 1), -1), max(min(diff[1], 1), -1)
                    if max(abs_diff) == 2:
                        knots[tail_idx] = (
                            knots[tail_idx][0] + correction[0],
                            knots[tail_idx][1] + correction[1],
                        )
                head_pos_acc.append(knots[0])
                tail_pos_acc.append(knots[-1])
    print(knots[0], knots[-1])
    print(len(set(head_pos_acc)), len(set(tail_pos_acc)))
