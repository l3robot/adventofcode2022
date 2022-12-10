def compute_cycles(register: int, cycle: int, strengths: list, tickers: list) -> None:
    if cycle in tickers:
        strengths.append(cycle * register)


if __name__ == "__main__":
    tickers = [20, 60, 100, 140, 180, 220]
    register, cycle, strengths = 1, 1, []
    with open("input.txt", "r") as f:
        for instr in f.readlines():
            cmd, *args = instr.strip("\n").split(" ")
            match cmd:
                case "addx":
                    cycle += 1
                    compute_cycles(register, cycle, strengths, tickers)
                    register += int(args[0])
                    cycle += 1
                    compute_cycles(register, cycle, strengths, tickers)
                case "noop":
                    cycle += 1
                    compute_cycles(register, cycle, strengths, tickers)
    print(strengths)
    print(sum(strengths))
