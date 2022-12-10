SCREEN_HEIGHT = 6
SCREEN_WIDTH = 40


def draw(sprite: int, cycle: int, screen: list) -> None:
    y_pos, x_pos = cycle // SCREEN_WIDTH, cycle % SCREEN_WIDTH
    if x_pos in range(sprite, sprite + 3):
        screen[y_pos][x_pos] = "#"


if __name__ == "__main__":
    sprite, cycle = 1, 1
    screen = [["."] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]
    with open("input.txt", "r") as f:
        for instr in f.readlines():
            cmd, *args = instr.strip("\n").split(" ")
            match cmd:
                case "addx":
                    cycle += 1
                    draw(sprite, cycle, screen)
                    sprite += int(args[0])
                    cycle += 1
                    draw(sprite, cycle, screen)
                case "noop":
                    cycle += 1
                    draw(sprite, cycle, screen)
    print("\n".join(["".join(row) for row in screen]))
