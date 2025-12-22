from collections import deque, defaultdict
from typing import List

"""
input: numCourses (number of courses you can take), preqreqs (list)
preqs -> [a_i, b_i] (must complete b_i @ index 1, before coruse a_i @ index 0)
function: caFinish -> determine if it's possible to finsh all courses
output: boolean(False, True)

Input: numCourses = 3, prerequisites = [[2, 1], [1, 0], [0, 2]]                                                   i
{
    1: 0,
    2: [1]
    3: []
} [ yes you can take these courses in this succession from 0 -> 2 ]

Output: True
Explanation: You can complete course 0 first, then course 1, and finally course 2.

Input: numCourses = 4, prerequisites = [[3, 2], [2, 1], [1, 0], [0, 3]]
Output: False
Explanation: The prerequisites form a cycle, making it impossible to finish all courses.
{

}

Input: numCourses = 5, prerequisites = [[4, 2], [3, 1], [2, 0]]
Output: True
Explanation: You can complete the courses in order from course 0 to course 4.

for i in range(n):
    graph -> dict
    you append values fo courses and then value is a list of prereqs

"""


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # kahn's algorithm
    q = deque()
    for i, degree in enumerate(degree):
        if degree == 0:
            q.append(i)

    visited_courses = 0
    queue = deque()
    while queue:
        node = queue.popleft()
        visited_courses += 1
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited_courses == num_courses


# O(n+m) -> only visiting a course at most once with n courses with m edges


# debug your code below
print(can_finish(4, [[1, 0], [2, 1], [3, 2]]))
