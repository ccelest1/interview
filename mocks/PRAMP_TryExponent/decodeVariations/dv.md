# 7/17/25

## Decode Variations

### Problem
> Letter can be encoded as follows 'A->1, B-2'.
> A message = string of uppercase letters, encoded first using the scheme -> 'AZB' = '1262'
> Given string of digits S from `0-9` represent encoded message, return ways to decode

### Analysis
- Input: message of type str
- Output: returns int of decode variations

- Algo Process
    - Restate Problem
        * Given a string in the form of integers -> return the possible ways characters can be returned

    - Goal of Function
        * take numbers and convert to corresponding characters

    - Types
        * str, int

    - Assertions and Assumptions
        * input string will be non-empty

    - Edge Cases (regardless of assertions, assumptions)
        * empty string, non numeric characters


#### Example \#1
```py
input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
```


#### Constraints
- `1 <= S.length <= 12`
- `output = type int`


#### Solution Code
[Py Solution](review.py)
#### TC, SC
- TC: O(n) -> n representing S, linear time
- SC: O(1) -> storing strings with variables in constant memory [ direct access ]

[JS Solution](decodeVariations.js)

### Neetcode
- [Neetcode Solution](nc.py)
#### TC, SC
