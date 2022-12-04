if __name__ == "__main__":
    priority = 0
    with open("input.txt", "r") as f:
        rucksacks = f.read().split("\n")
    for group_idx in range(0, len(rucksacks), 3):
        group = rucksacks[group_idx : group_idx + 3]
        if len(group) < 3:
            continue
        for item in group[0]:
            if item in group[1] and item in group[2]:
                break
        if item.islower():
            ord_item = ord(item) - ord("a") + 1
        else:
            ord_item = ord(item) - ord("A") + 27
        priority += ord_item
        print(group, item, ord_item)
    print(priority)
