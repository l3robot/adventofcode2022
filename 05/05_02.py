import re
from collections import defaultdict


def build_stacks(stacks_str):
    stacks = defaultdict(list)
    pattern = r" {3} |\[[A-Z]\]"
    for row in stacks_str.split("\n"):
        for i, item in enumerate(re.findall(pattern, row)):
            if item != "    ":
                stacks[i + 1].insert(0, item)
    return stacks


def print_stacks(stacks):
    num_stacks = len(stacks)
    max_size = max([len(v) for v in stacks.values()])
    stacks_str = []
    for i in range(max_size):
        idx = max_size - i - 1
        extracted = [
            stacks[j + 1][idx] if len(stacks[j + 1]) > idx else None
            for j in range(num_stacks)
        ]
        row_str = " ".join(["   " if j is None else j for j in extracted])
        stacks_str.append(row_str)
    stacks_str.append(" ".join([f" {i+1} " for i in range(num_stacks)]))
    print("\n".join(stacks_str))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        content = f.read()
    stacks_str, moves_str = content.split("\n\n")
    stacks = build_stacks(stacks_str)
    move_pattern = r"^move ([0-9]+) from ([0-9]+) to ([0-9]+)"
    for move_str in moves_str.split("\n"):
        if len(move_str) == 0:
            continue
        num, from_stack, to_stack = re.findall(move_pattern, move_str)[0]
        num, from_stack, to_stack = int(num), int(from_stack), int(to_stack)
        item = stacks[from_stack][-num:]
        stacks[from_stack] = stacks[from_stack][:-num]
        stacks[to_stack] += item
    print_stacks(stacks)
    print("".join([stacks[i + 1][-1][1] for i in range(len(stacks))]))
