# 11.27.25

## [The Award Budget Cuts Problem](https://www.tryexponent.com/practice/prepare/award-budget-cuts)

### Problem:
#### 1st Part
- Awards committee of alma mater asked for assistance in budget allocation problem they are facing
- Budget is now reduced to `newBudget` and req reallocation of grants
- Committee made decision that they want to impact the fewest grant recipients as possible with a max `cap` on all grants
- Every grant planned to be higher than `cap` will be exactly $`cap`
- Grants less or equal to `cap` won't be impacted
#### 2nd Part
- Given list[] `grantsArray` of original grants and reduced budget `newBudget` write a fn `findGrantsCap` that determines most efficient `cap` that can be instituted to
    1. impact the least number of recipients
    2. meet new budget constraint -> `N` = length of `grantsArray`, Sum of `N` grants = `newBudget`
        * `sum(grantsArray) <= newBudget`


### Analysis
- Input:
    * list[] `grantsArray`
    * int `newBudget`
- Output:

- Algo Process
    - Restate Problem:
        Budget problem and need to determine best cap

    - Goal of Function
        * Find the cap with the minimal impact on initial grants given the newBudget constraint

    - Types
        * list[int], int

    - Assertions and Assumptions
        * `0 <= grantsArray.length <= 20`
            - grantsArray will always be between length 0 and 20
        * `0 <= grantsArray[i]`
            - no negative grants

    - Edge Cases (regardless of assertions, assumptions)
        * handle empty grantsArray
        * handle if grantsArray current sum is less than newBudget


#### Example \#1
```py
input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
```
### Notes
Key Insight or my thinking:
- For this problem, we should sort the grants
- By sorting we can then iteratively determine which grants are small enough to be unaffected by the cap
- For each small grant encountered, we know that it won't be capped -> subtract that grant from the budget and recalc cap for remaining grants
- Once we hit a grant that's larger than current cap estimate, we found answer as all next grants are also capped at that value

#### Time, Space Complexity
- TC:
    * O(n log n) for sorting -> ascending order for n elements in grantsArray of length n
- SC:
    * O(1) -> constant space for integers

#### Optimizations
- Can't do better than O(n log n) -> due to constraint of comparison based sorting

#### Multiple Solutions
- Req max cap for least impact and algo finds it due to greedy exclusion of smaller grants to max cap for remaining grants

## Rationale
- Partition grants into 'below cap' and 'at cap' groups
- Through sorting and iteration, find optimal partition to max cap and respect budget constraint
- Cap = remBudget / affected
