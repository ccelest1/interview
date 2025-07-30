"""
grantsArray: list[int] => original grants amounts
newBudget: int
findGrantscap -> finds cap amount for grants, impacts least number of recipients
return int(cap)

[ ] -> stores new grants based on the given newBudget, CB = []
sum(CB) <= int(newBudget)

grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
[2, 47, 47, 47, 47] <- CB -> sum(CB) -> 190
Ouput: 47 <- cap placed in order to be equal to newBudget

(0) edge case - if the empty array, or new Budget -> 0
[2] -> budget 1: [1]
(1) Determine if original array i less than or equal to amount (skip) [sum]
(2) sorted(array)-> iterate through -> 2 -> newBudget = 188, 50 -> 138 -> 120 -> 18 -> 100 exceeds
minThreshold - [2,.., ..], [2, 50, ..]
...
(3) return array
"""

from typing import List


def find_grants_cap(grantsArray: List[int], newBudget: int) -> float:
    # edge cases
    if not grantsArray or not newBudget:
        return
    if sum(grantsArray) <= newBudget:
        return grantsArray

    # handling cases where we have exceedance
    res = []
    for i in range(len(grantsArray)):
        """
        nGA = sorted(grantsArray, reverse=True)
        [2, 100, 50, 120, 1000] > [1000, 120, 100, 50, 2] - 190
        188 -> 138 -> 118

        We define a surplus variable that represents the excess amount we need to cut back:
        surplus = sum(grantsArray) - newBudget
        Iterative Process
        We iteratively subtract from surplus the amount each grant saves us if it were capped at the next lower level. Our goal is to find when surplus ≤ 0.
        Mathematical Formula
        For each iteration i, we calculate:
        surplus[i] = surplus[i-1] - (i+1) × (grantsArray[i] - grantsArray[i+1])

        Example Walkthrough
        Given: grantsArray = [1000, 120, 100, 50, 2], newBudget = 190
        Initial surplus: 1272 - 190 = 1082
        Iteration 0: surplus₀ = 1082
        Iteration 1: surplus₁ = 1082 - 1×(1000-120) = 1082 - 880 = 202
        Iteration 2: surplus₂ = 202 - 2×(120-100) = 202 - 40 = 162
        Iteration 3: surplus₃ = 162 - 3×(100-50) = 162 - 150 = 12
        Iteration 4: surplus₄ = 12 - 4×(50-2) = 12 - 192 = -180 ✓
        Exact cap: 2 + (-(-180)/4) = 2 + 45 = 47
        2 + 50 + (136/3)
        """
