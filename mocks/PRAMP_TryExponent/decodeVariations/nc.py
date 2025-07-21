"""
letter can be encoded from its character to a number value where A:1,...,Z:26
String of uppercase letters, encoded first using scheme of 'AZB' -> '1262"
Given string of digits S with each integer in range of 0-0, return number of ways to decode particular given S

input: S = '1262' -> output: 3
ex: there are 3 messages that encode to '1262' being 'AZB', 'ABFB', 'LFB'
"""

"""
given a specified string, there are a number of branching paths for string combo generation between 1 to 26
"""
# ask either dp[i] = dp[i+1] + dp[i+2] due to branching representing multiple possibilities
# recursive caching O(n) tc solution


class Solution:
    # recursive - top down (recursive + memoization)
    def NumDecoding(s: str) -> int:
        # define base case for cache
        dp = {len(s): 1}

        def dfs(i):
            # is is already cached or string end
            if i in dp:
                return dp[i]
            # if string starts with 0 then its invalid - assumption
            if s[i] == "0":
                return 0

            # if not 0, then through 1 to 9, then take val as single digit
            res = dfs(i + 1)

            # if single char comes after current (if i+1 in bounds), or it starts with 1 or 2 and its within the range of 0 to 6
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and int(s[i + 1]) <= 6):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)

    # iterative - bottom up (iterative + tabulation)
    def NumDecoding2(s: str) -> int:
        N = len(s)
        dp = {N: 1}
        for i in range(N - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < N and (s[i] == "1" or s[i] == "2" and int(s[i + 1]) <= 6):
                dp[i] += dp[i + 2]
        return dp[0]


print(Solution.NumDecoding2("1262"))
print(Solution.NumDecoding2("0262"))
print(Solution.NumDecoding2("1260"))
print(Solution.NumDecoding2("1062"))
