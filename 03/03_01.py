if __name__ == "__main__":
    priority = 0
    with open("input.txt", "r") as f:
        for rucksack in f.readlines():
            rucksack = rucksack.strip("\n")
            mid = len(rucksack) // 2
            compartment1, compartment2 = rucksack[:mid], rucksack[mid:]
            for item in compartment1:
                if item in compartment2:
                    break
            if item.islower():
                ord_item = ord(item) - ord("a") + 1
            else:
                ord_item = ord(item) - ord("A") + 27
            priority += ord_item
            print(compartment1, compartment2, item, ord_item)
    print(priority)
