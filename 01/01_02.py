if __name__ == "__main__":
    with open("input.txt", "r") as f:
        elf_desc = f.read()
    ptr, max_cals = [], []
    for elf_id, foods in enumerate(elf_desc.split("\n\n")):
        cals = sum([int(cal.strip("\n")) for cal in foods.split("\n") if cal])
        ptr.append(elf_id)
        max_cals.append(cals)
        idx = sorted(range(len(ptr)), key=max_cals.__getitem__)[::-1]
        ptr = [ptr[i] for i in idx[:3]]
        max_cals = [max_cals[i] for i in idx[:3]]
    print(ptr, max_cals)
    print(sum(max_cals))
