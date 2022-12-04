if __name__ == "__main__":
    with open("input.txt", "r") as f:
        elf_desc = f.read()
    ptr, max_cals = 0, 0
    for elf_id, foods in enumerate(elf_desc.split("\n\n")):
        cals = sum([int(cal.strip("\n")) for cal in foods.split("\n") if cal])
        if cals > max_cals:
            ptr, max_cals = elf_id, cals
    print(ptr, max_cals)
