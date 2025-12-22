"""
input:
two strings (text, pattern)
output: boolean -> true or false
goal of function:
is_match supporting (regex functionality) the '.' (wildcard -> single char)
'*' (matched for a 0 or more sequence of prev letter)

flag = False
if text[i]!== pattern[i]:
     p
first impression: iterate through string, and (1) detect if we encounter a ., * (pattern)
if pattern[i] === "." :
    continue
(2). if we don't encounter then we can ask if the two strings are = and then return if true
return Falg

input:  text = "aa", pattern = "a"
                 i
output: false
-> does not include the spec, and aren't same strings


input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
flag = True
                  i                i

output: true

input:  text = "abbb", pattern = "ab*"
                  i                 i
return True if we have flag set to True a nd we enocunter a *
output: true

input:  text = "acd", pattern = "ab*c."
i -> if we encountered the same chars -> and then we get to a char that is mismatch
and we detect a star, skip to next element in the pattern and then i+=1
output: true
"""


def is_match(text: str, pattern: str) -> bool:
    # edge cases
    if not text or not pattern:
        return False

    pos = 0

    def regex_recursion(s, pattern, pos):
        # base case 1 - if we reach of end array
        if pos == len(s) - 1 or pos == len(pattern) - 1:
            return True
        # bc 2?
        if s[pos] != pattern[pos] and pattern[pos] != ".":
            return False

        pos += 1
        # input:  text = "abbb", pattern = "ab*"
        regex_recursion(s, pattern, pos)

    return regex_recursion(text, pattern, pos)


# debug your code below
print(is_match("aa", "a"))

# https://www.youtube.com/watch?v=gK8KmTDtX8E
# https://www.youtube.com/watch?v=NA7u5GTh6fw


def is_match2(text: str, pattern: str) -> bool:

    # edge cases
    if not text or not pattern:
        return False

    i, j = 0, 0

    def regex_recursion(s, p, i, j):
        # bc1
        if j == len(p):
            return i == len(s)

        # bc2
        if i == len(s) - 1:
            pass

        first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

        # handling star
        if j + 1 < len(p) and p[j + 1] == "*":
            if not first_match:
                regex_recursion(s, p, i, j + 2)
            if first_match:
                regex_recursion(s, p, i + 1, j)
        else:
            if p[j] == s[i]:
                regex_recursion(s, p, i + 1, j + 1)
            else:
                return False

        # input:  text = "abbb", pattern = "ab*"
        return regex_recursion(s, p, i, j)

    return regex_recursion(text, p, i, j)
