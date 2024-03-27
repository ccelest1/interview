"""
"""


def destinations(teleporters, sides, start_pos, board_end):
    # only uniqe destinations
    unique = set()
    tracker = {}
    # O(T)
    for teleport in teleporters:
        teleport_split = teleport.split(",")
        tracker[int(teleport_split[0])] = int(teleport_split[1])
    # O(S)
    for roll in range(1, sides + 1):
        potential_d = (start_pos + roll) % (board_end + 1)
        if potential_d in tracker:
            unique.add(tracker[potential_d])
        else:
            unique.add(potential_d)
    return list(unique)


print(destinations(["3,1", "4,2", "5,10"], 6, 0, 20))


def finishable(teleporters, sides, start_pos, board_end):
    tracker = {}
    # O(T)
    for teleport in teleporters:
        teleport_split = teleport.split(",")
        tracker[int(teleport_split[0])] = int(teleport_split[1])

    def f_recurse(portals, die, current, end, visited):
        # if we reached ideal condition
        for roll in range(die):
            if current + roll == end or current + roll > end:
                return True

        # if we have run out of possible rolls
        if die == 0:
            return False

        # roll
        for roll in range(1, sides + 1):
            new_pos = current + roll

            # ask if in teleporters
            if new_pos in portals:
                new_pos = portals[new_pos]

            # eval if less than end of board and if not in visited
            if new_pos <= board_end and new_pos not in visited:
                visited.add(new_pos)
                if f_recurse(tracker, die - 1, new_pos, board_end, visited):
                    return True
                visited.remove(new_pos)
        return False

    visited = set()
    visited.add(start_pos)

    return f_recurse(tracker, sides, start_pos, board_end, visited)


teleporters1 = ["3,1", "4,2", "5,10"]
print(finishable(teleporters1, 4, 0, 20))
teleporters2 = ["5,10", "6,22", "39,40", "40,49", "47,29"]
print(finishable(teleporters2, 4, 0, 20))
