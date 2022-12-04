if __name__ == "__main__":
    cnt = 0
    with open("input.txt", "r") as f:
        for pair in f.readlines():
            pair = pair.strip("\n")
            elf1, elf2 = pair.split(",")
            elf1, elf2 = elf1.split("-"), elf2.split("-")
            elf1 = [int(elf1[0]), int(elf1[1])]
            elf2 = [int(elf2[0]), int(elf2[1])]
            elf1, elf2 = (elf1, elf2) if elf1[0] <= elf2[0] else (elf2, elf1)
            range1 = list(range(elf1[0], elf1[1] + 1))
            repr1 = "".join(["+" if i in range1 else "." for i in range(100)])
            range2 = list(range(elf2[0], elf2[1] + 1))
            repr2 = "".join(["+" if i in range2 else "." for i in range(100)])
            if elf1[1] >= elf2[0]:
                print(repr1, " OK ")
                print(repr2, " OK ")
                cnt += 1
            else:
                print(repr1)
                print(repr2)
            print("-" * 100)
    print(cnt)
