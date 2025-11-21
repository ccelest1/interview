# PART 1
# You're a taxi on an infinite 2D Cartesian grid.
# You start at a location and must reach destination.
# Some cells are blocked by obstacles; you may not go on them.
# There are a finite number of obstacles
# On each move you can go one cell U (up), D (down), L (left), or R (right).

# Task: Define a function that will return any one of the shortest valid path from start to destination as a string over {U,D,L,R}.

# Example to test:
# y=3   .   .   .   .   .
# y=2   .   .   .   X   D
# y=1   C   .   .   X   .
# y=0   .   .   X   X   .
# y=-1  .   X   .   .   .
# y=-2 -1   0   1   2   (x)

# valid output: "RRUURRD"

# PART 2
# We now add parades to the grid.
# - A parade is defined by a starting cell and a direction
# - The parade blocks the starting cell and all cells extending infinitely in that direction.
# - The taxi cannot step on or cross any parade cell.
# Other rules remain the same: you start at C, want to reach D, and must avoid both obstacles and parades.

# Example to test:
# y=3   .   ^   .   .   .   .
# y=2   C   ^   .   .   .   .
# y=1   .   ^   X   .   V   .
# y=0   .   .   .   .   V   D
# y=-1  .   .   .   .   V   .
#      -2  -1   0   1   2   3  (x)
#
# valid output: DDRRRUURRDD


2, 1
2  0
2, -1'

[2, (1, [0, -1]




from collections import deque
"""
C = start
D = destination
x = obstacle
"""


def shortest_path(x, y, dest_x, dest_y, obstacles):

    path = ''

    q = deque()
    q.append((x, y, '', set()))

    dir = [[0, 1, 'U'], [1, 0, 'R'], [-1,0, 'L'], [0, -1, 'D']]

    while q:

        curx, cury, cur_path, visited = q.popleft()
        print("curx, cury, cur_path", curx, cury, cur_path)

        if (curx, cury) in visited:
            print('curx, cury is already in path')
            continue

        visited.add((curx, cury))

        if (curx, cury) in obstacles:
            print('curx, cury is blocked')
            continue

        if (curx, cury) == (dest_x, dest_y):
            print("found destination")
            return cur_path

        for dx, dy, dc in dir:
            nx, ny = dx + curx, dy + cury
            updated_path = cur_path+dc

            print("nx, ny, updated_path", nx, ny, updated_path)

            q.append((nx, ny, updated_path, visited))

    return path


obstacles = {(2, 2),(2,1), (2,0), (1, 0), (0, -1)}

shortest_path(-1, 1, 3, 2, obstacles)
