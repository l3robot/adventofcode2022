from collections import Counter
from typing import Optional


def execute_cd(location_instr: str, location: list):
    if location_instr == "/":
        location.clear()
        location.append("/")
    elif location_instr == "..":
        location.pop()
    else:
        old_location = "" if location[-1] == "/" else location[-1]
        new_location = "/".join([old_location, location_instr])
        location.append(new_location)


def execute_command(command: list, location: list):
    match command[0]:
        case "cd":
            execute_cd(command[1], location)
        case "ls":
            pass


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        location = ["/"]
        dirs = Counter()
        for line in f.readlines():
            line = line.strip("\n")
            parts = line.split(" ")
            if parts[0] == "$":
                execute_command(parts[1:], location)
            else:
                if parts[0] != "dir":
                    size, filename = parts
                    for dir in location:
                        dirs[dir] += int(size)
    to_freed = dirs["/"] - 40000000
    sizes = list(filter(lambda x: x >= to_freed, sorted(dirs.values())))
    print(sizes[0])
