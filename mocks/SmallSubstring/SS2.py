def hasAll(arr, str):
    for i in arr:
        if i not in str:
            return False
    return True


def get_shortest_unique_substring(arr, str):
    n = len(arr)
    nStr = len(str)
    S = ""
    if nStr < n or not hasAll(arr, str):
        return ""
    # iterate through long string
    for s in range(nStr):
        # starts from length of array of chars till end of string
        for e in range(s + n, nStr + 1):
            subS = str[s:e]
            # if we find a lesser optimal substring and we have a current min substring
            if (len(subS) >= len(S)) and (len(S) != 0):
                break
            # if we haven't found substring that contains all chars in array, continue looking
            if not hasAll(arr, subS):
                continue
            # if we find an exact match, we know its most optimal
            if len(subS) == n:
                return subS
            # update for optimal substring
            S = subS
            break
    return S


print(get_shortest_unique_substring(["x", "y", "z"], "xyyzayxyx"))
