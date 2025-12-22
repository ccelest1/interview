def findGrantsCap(grantsArray: list[int], mewBudget: int):

    # get length for iteration
    N = len(grantsArray)

    # avoid zero division
    if N == 0:
        return 0

    # sort in increasing order - O(n log n)
    grantsArray.sort()

    # if we have an array where the sum of the budgets is less than or equal to newBudget, return the largest value -> end of sorted array
    if sum(grantsArray) <= newBudget:
        return grantsArray[N-1]

    # storing count of grants impacted
    # assume everyone is impacted at start
    affectedCount = N

    '''
    RB -> While traversing array, update remBudget to reflect remaining Budget for allocation
    DRB -> Starting assumption that all grants will be impacted and divide rem budget equally if not then update number
    '''
    remainingBudget = newBudget
    dividedRemBudget = remainingBudget / affectedCount

    for grant in grantsArray:
        if grant < dividedRemBudget:
            '''
            if current grant < cap lower bound, current grant won't be impacted, subtract 1 from affectedCount
            '''
            affectedCount -= 1
            '''
            update remaining budget for remaining grants -> subtract current grant as it won't be impacted
            then recompute lower bound with remaining grants
            '''
            remainingBudget -= grant
            dividedRemBudget = remainingBudget / affectedCount
        else:

            break

    return dividedRemBudget


grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(findGrantsCap(grantsArray, newBudget))
'''
2, 50, 120, 100, 1000
   i (break)
AC = 5 -> 4
RB = 190 -> 188
    dividedRemBudget = remainingBudget / affectedCount
DRB = 38 -> 47 (return)
'''
