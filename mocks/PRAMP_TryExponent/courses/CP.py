def can_finish(numCourses: int, preRequisites: list[int]):
    # creating map that contains all the courses with an array to include preqs that have to be taken
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in preRequisites:
        preMap[crs].append(pre)

    # detecting loops
    visitSet = set()

    def dfs(crs):
        # bc: if we detect loop, then return False
        if crs in visitSet:
            return False
        # bc: if prereqs = empty list, return True -> can be def completed
        if preMap[crs] == []:
            return True

        # discovering course, pre-reqs for first time
        visitSet.add(crs)
        # run dfs on each pre -> if it returns False (if one course can't be completed -> if it does not execute)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        # remove from visitSet, already done doing so
        visitSet.remove(crs)
        # since course can be visited, set preMap to empty list -> if we run dfs again, execute and return true immediately
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


# PRAMP VERSION

"""
(1) create a dict that has the courses and the pre-reqs in the list as a key-value pair
(2) going to intialize an empty deque that represents visited nodes
(3) dfs (search through nodes and their children) ->
bcs:
        -> bc: if we find a node in the visited, return false
        -> bc: if we find node with no courses return True
        add -> deque.append()
        traverse -> dfs(preMap[crs])
        Micro-Op: preMap[crs] = []
        pop -> deque.pop()
(4) iterate using dfs with range(num_courses) as the courses are in range [0, n-1]
    -> if not dfs(crs): F, T
"""

from collections import deque, defaultdict
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:

    preMap = defaultdict(list)
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visited = deque()

    def dfs(crs):
        if crs in visited:
            return False
        if preMap[crs] == []:
            return True

        visited.append(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visited.pop()
        preMap[crs] = []
        return True

    for crs in range(num_courses):
        if not dfs(crs):
            return False
    return True


print(can_finish(4, [[1, 0], [2, 1], [3, 2]]))
print(can_finish(3, [[2, 1], [1, 0]]))
print(can_finish(4, [[3, 2], [2, 1], [1, 0], [0, 3]]))
print(can_finish(5, [[4, 2], [3, 1], [2, 0]]))
