# actual solution
"""
Solution 1:
    Perform linear operation on arr while pushing copy of every char to stack, then pull them in rev order while copying words back into arr
Solution 2:
    Initialize new array at same length of arr
    Iterate over arr from right to left and copy any sequency of chars to new array from left to right

Both approaches take O(N) time, at least O(N) space

More elegant and efficient approach:
    Reverse chars in arr and then rev chars in words separately
    While first rev provides words in rev order as desired it also reverses chars of each word
    To fix: perform second rev on each word separately

Reversing array items performed by mirror function, swap items of every 2 indices with same distance from middle
"""


class Solution:
    def reverse_words(arr):
        if not arr:
            return None
        N = len(arr) - 1

        # Function to reverse characters in a substring
        def reverse_substr(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Reverse the entire array
        reverse_substr(arr, 0, N - 1)

        # Reverse characters within each word
        wordStart = 0
        for i in range(0, N):
            if arr[i] == " ":
                # if we encounter a word that had one preceding
                if wordStart:
                    reverse_substr(arr, wordStart, i - 1)
                    wordStart = None
                # if we encounter the last word that would be in reverse sentence
            elif i == N - 1:
                if wordStart:
                    reverse_substr(arr, wordStart, i)
                # if we haven't started reverse process i.e we need to get to start
            else:
                if not wordStart:
                    wordStart = i

        return arr


print(
    Solution.reverse_words(
        [
            "p",
            "e",
            "r",
            "f",
            "e",
            "c",
            "t",
            "  ",
            "m",
            "a",
            "k",
            "e",
            "s",
            "  ",
            "p",
            "r",
            "a",
            "c",
            "t",
            "i",
            "c",
            "e",
        ]
    )
)
