if __name__ == "__main__":
    cnt = 0
    with open("input.txt", "r") as f:
        for pair in f.readlines():
            pair = pair.strip("\n")
            elf1, elf2 = pair.split(",")
            elf1, elf2 = elf1.split("-"), elf2.split("-")
            elf1 = [int(elf1[0]), int(elf1[1])]
            elf1_size = elf1[1] - elf1[0]
            elf2 = [int(elf2[0]), int(elf2[1])]
            elf2_size = elf2[1] - elf2[0]
            elf1, elf2 = (elf1, elf2) if elf1_size <= elf2_size else (elf2, elf1)
            if (elf1[0] >= elf2[0]) and (elf1[1] <= elf2[1]):
                print(pair)
                cnt += 1
    print(cnt)
