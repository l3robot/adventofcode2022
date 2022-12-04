# decoders
decoder = {
    "A": 1,
    "B": 2,
    "C": 3,
}
points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
strategy = {
    "X": lambda player1: ((player1 - 1) - 1) % 3 + 1,
    "Y": lambda player1: player1,
    "Z": lambda player1: ((player1 - 1) + 1) % 3 + 1,
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
            player1 = decoder[player1]
            outcome_pts = points[player2]
            print(player2)
            player2 = strategy[player2](player1)
            pts += outcome_pts + player2
            print(names[player1], names[player2], outcome_pts)
    print(pts)
