# rules
loss = lambda diff: (diff == -1) or (diff == 2)
draw = lambda diff: diff == 0
win = lambda diff: (diff == 1) or (diff == -2)

# decoders
strategy = {
    "A": 1,
    "B": 2,
    "C": 3,
    # Strategy:
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# Names
names = {
    1: "rock",
    2: "paper",
    3: "scissors",
}

if __name__ == "__main__":
    pts = 0
    with open("input.txt", "r") as f:
        for round in f.readlines():
            player1, player2 = round.strip("\n").split(" ")
            player1 = strategy[player1]
            player2 = strategy[player2]
            diff = player2 - player1
            if loss(diff):
                pts += player2 + 0
                print(names[player1], names[player2], diff, "loss")
            elif draw(diff):
                pts += player2 + 3
                print(names[player1], names[player2], diff, "draw")
            elif win(diff):
                pts += player2 + 6
                print(names[player1], names[player2], diff, "win")
    print(pts)
