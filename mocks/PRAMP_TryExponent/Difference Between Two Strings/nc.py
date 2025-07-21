"""
Dynamic Programming problem that is related Least Common Substring
Notes:
horse -> ros
[-H, +R, O, -R, S, -E]

Problem ops: able to insert a char, delete a char, replace a char btwn both strings
Ex:
    If word1 and word2 are the same, then number of ops = 0
    if word1 is abc and word2 is empty, then min # of ops is length of word1 and vice versa
    if we find differences in both strings,
        sub case 1: we find char similarities, but find differences following:
          if w1[i]==w2[j]: res.append(w2[j]), i+=1, j+=1
          else:
            insert - (i, j+1) -> res.append(f"+{target[j]}")
            delete - (i+1, j) -> res.append(f"-{source[i]}")
            replace - (i+1. j+1) source[i]=target[j] -> res.append(f"-{source[i]}"), res.append(f"+{target[j]}")
    going to implement cache that allows us to understand minimum number of changes required
"""


class Solution:
    def minDistance(source: str, target: str) -> int:
        res = []
        cache = [[float("inf")] * (len(source) + 1)] * (len(target) + 1)

        for j in range(len(target) + 1):
            cache[len(source)][j] = len(target) - j
        for i in range(len(source) + 1):
            cache[len(target)][i] = len(source) - i

        for i in range(len(source) - 1, -1, -1):
            for j in range(len(target) - 1, -1, -1):
                if source[i] == target[j]:
                    res.append(f"+{target[j]}")
                else:
                    # evaluating which move provides us with a min transaction step
                    eval_min = min(
                        cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1]
                    )
                    if eval_min == cache[i + 1][j]:
                        res.append(f"+{target[j]}")
                        cache[i][j] = 1 + eval_min
                    elif eval_min == cache[i][j + 1]:
                        res.append(f"-{source[i]}")
                        cache[i][j] = 1 + eval_min
                    else:
                        res.append(f"-{source[i]}")
                        res.append(f"+{target[j]}")
                        cache[i][j] = 1 + eval_min

        # rip
        print(res)
        return cache[0][0]


print(Solution.minDistance("abc", "cba"))
