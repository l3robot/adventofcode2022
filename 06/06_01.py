MESSAGE_SIZE = 4


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        message = f.read()
    for idx in range(len(message) - MESSAGE_SIZE):
        markers = message[idx : idx + MESSAGE_SIZE]
        if len(set(markers)) == MESSAGE_SIZE:
            break
    print(idx + MESSAGE_SIZE)
