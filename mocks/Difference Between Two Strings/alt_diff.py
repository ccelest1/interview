"""
//problem
given two strings of uppercase letters 'source', 'target', list a sequence of edits to convert source to target using the lest edits i.e return min(edits)

Example: source = 'ABCDEF', target = 'ABDFFGH' - > edits = ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]- for tokens that are similar to target and source append token, for token not present in target but in source -token, for token present in target but not in source +token

if there are multiple answers, use answer that favors removing from source first

"""


class Solution:
    def DBTS(source, target):
        ans = []
        i, j = 0, 0
        memo = [[0] * len(source)] * len(target)

        def dp(i, j):
            # if one of strings is empty -> return length of target - current pointer ?
            if i == len(source) or j == len(target):
                return len(target) - j
            elif not memo[i][j]:
                # no cached answer, find one
                if source[i] == target[j]:
                    memo[i][j] = dp(i + 1, j + 1)
                else:
                    memo[i][j] = 1 + min(dp(i + 1, j), dp(i, j + 1))
            return memo[i][j]

        while i < len(source) and j < len(target):
            # if chars in both strings are equal, add char and increment both pointers
            if source[i] == target[j]:
                ans.append(source[i])
                i += 1
                j += 1
            else:
                # determine if we have to add token with subtract from source/add from target
                if dp(i + 1, j) <= dp(i, j + 1):
                    ans.append(f"-{source[i]}")
                    i += 1
                else:
                    ans.append(f"+{target[j]}")
                    j += 1

        while j < len(target):
            ans.append(f"+{target[j]}")
            j += 1

        return " ".join(ans)


print(Solution.DBTS("ABCDEF", "ABDFFGH"))
