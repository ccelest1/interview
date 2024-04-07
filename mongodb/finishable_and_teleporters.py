"""
Thrilling Teleporters allows players to randomize the teleporters each game. However, during development they found that sometimes this can lead to boards where a player cannot get to the end of the board. We want to figure out if this has happened.

You'll be given the following inputs:
- A collection of teleporter strings
- The number of sides on the die
- The square the player starts on
- The last square on the board

Write a function that returns whether or not it is possible to get to the last square from the starting square in any number of turns.

Examples:
teleporters1 = ["10,8", "11,5", "12,7", "13,9"]
               +------------------+
               |        +-----+   |
               v        v     |   |
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
                     ^     ^          |   |
                     +-----|----------+   |
                           +--------------+
finishable(teleporters1, 4, 0, 20)
["10,8", "11,5", "12,7", "13,9", "2,15"]
0->2 (2)
2->15 (tp)
15->16 (1)
16->20 (4)

With a 4 sided die, starting at square 0 with a board ending at square 20 (as pictured above)
No matter what you roll, it's not possible to get past the teleporters from 10-13.
finishable(teleporters1, 4, 0, 20) => False

If an additional teleporter was added from square 2 to square 15, this would be possible to finish.
teleporters2 = ["10,8", "11,5", "12,7", "13,9", "2,15"]
finishable(teleporters2, 4, 0, 20) => True

But if we started on square 9, then it is still impossible as square 20 cannot be reached.
finishable(teleporters2, 4, 9, 20) => False

Additional Input:
teleporters3 = ["10,8", "11,5", "12,1", "13,9", "2,15"]
teleporters4 = ["2,4", "9,8", "11,7", "12,6", "18,14",
                "19,16", "20,9", "21,14", "22,6", "23,26",
                "25,10", "28,19", "29,27", "31,29", "38,33",
                "39,17", "41,30", "42,28", "45,44", "46,36"]
teleporters5 = ["4,21", "11,18", "13,17", "16,17", "18,21",
                "22,11", "26,25", "27,9", "31,38", "32,43",
                "34,19", "35,19", "36,39", "38,25", "41,31"]

Complexity variable:
B = size of the board
Note: The number of teleporters, T, and the size of the die, D, are bounded by B.

All Test Cases:
                        die, start, end
finishable(teleporters1, 4,   0,    20)  => False (Above)
finishable(teleporters2, 4,   0,    20)  => True  (Above)
finishable(teleporters2, 4,   9,    20)  => False (Above)
finishable(teleporters3, 4,   9,    20)  => True
finishable(teleporters4, 4,   0,    50)  => False
finishable(teleporters4, 6,   0,    50)  => True
finishable(teleporters5, 4,   0,    50)  => True
finishable(teleporters5, 2,   0,    50)  => False

(1) understand the outcomes
(2) starting position
(3) source -> end based on ts (outcomes, confied by the particular die)
(4) based on outcome, find if outcome + (either) additonal dice roll
"""


def finishable(teleporters, sides, start_pos, board_end):
    possible_dice_rolls = [i for i in range(1, sides + 1)]
    outcomes = []
    # O(D)
    for roll in possible_dice_rolls:
        outcomes.append(start_pos + roll)
    tracker = {}
    # O(T)
    for teleport in teleporters:
        teleport_split = teleport.split(",")
        tracker[int(teleport_split[0])] = int(teleport_split[1])

    visited = []

    def visiting(visited, starting_side, end_side, pos):
        if board_end in visited:
            return True
        # handle reaching board end
        if pos >= board_end:
            return True
        if pos in tracker:
            return visiting(visited, starting_side, end_side, tracker[pos])
        new_pos = pos + starting_side
        if new_pos not in visited and starting_side != end_side:
            visited.append(new_pos)
            if visiting(visited, starting_side, end_side, new_pos):
                return True
        return False

    return visiting(visited, 1, sides, start_pos)

    # visited = [start_pos]
    # while l < sides:
    #     pos = 0
    #     for outcome in outcomes:
    #         outcome += l
    #         if outcome in tracker:
    #             pos = tracker[outcome]
    #         visited.append(outcome)
    #         print(visited)
    #     if visited[-1] == board_end:
    #         return True
    #     l += 1


teleporters1 = ["3,1", "4,2", "5,10"]
print(finishable(teleporters1, 4, 0, 20))
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
print(finishable(teleporters2, 4, 0, 20))


def destinations(teleporters, sides, start_pos, board_end):
    outcomes = [i + start_pos for i in range(1, sides + 1)]
    tracker = {}
    # O(T)
    for teleport in teleporters:
        teleport_split = teleport.split(",")
        tracker[int(teleport_split[0])] = int(teleport_split[1])
    res = []
    # bounded by B -> O(B)
    for outcome in outcomes:
        if outcome <= board_end:
            if outcome in tracker:
                res.append(tracker[outcome])
            else:
                res.append(outcome)
    return list(set(res))


teleporters1 = ["3,1", "4,2", "5,10"]
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
teleporters3 = [
    "6,18",
    "36,26",
    "41,21",
    "49,55",
    "54,52",
    "71,58",
    "74,77",
    "78,76",
    "80,73",
    "92,85",
]
teleporters4 = [
    "97,93",
    "99,81",
    "36,33",
    "92,59",
    "17,3",
    "82,75",
    "4,1",
    "84,79",
    "54,4",
    "88,53",
    "91,37",
    "60,57",
    "61,7",
    "62,51",
    "31,19",
]
teleporters5 = ["3,8", "8,9", "9,3"]

# print(destinations(teleporters2,  6,   46,   100))
# print(destinations(teleporters2, 10,    0,    50))
# print(destinations(teleporters3, 10,   95,   100))
# print(destinations(teleporters3, 10,   70,   100))
# print(destinations(teleporters4,  6,    0,   100))
# print(destinations(teleporters5,  7,    2,    20))
# print(destinations(teleporters1,  6,    0,    20))
