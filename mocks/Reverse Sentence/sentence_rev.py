"""
arr will never be empty, if(!arr) return
' '. (split on characters, also include spaces)
assume there is no punctuation
assuming where a word starts and ends is based on where space occurs

ex2:
 input
  'y', 'o', 'u', " ' ", "r", "e",
  "n", "i", "c", "e"
  output
  "n", "i", "c", "e"
  'y', 'o', 'u', " ' ", "r", "e"

  [
   p " " m "" p -> perfect "" makes -> perfect
  ]


  input = arr
  output = []
iterate through string
 start from end of string, find where spaces occur (i = " "[index of space], j= [end of array]),
   output.push(input[i+1:j])
 throughout iterations, update input to be the characters we wouldn't consider
"""

"""
tc:O(n^2)
sc:O(n)
"""

# breaks on
"""
Test Case #2
Input:
["a"," "," ","b"]
Expected:
["b"," "," ","a"]

Actual:

['a', ' ', ' ', 'b']
"""


def reverse_words(arr):
    input_arr = arr
    output = []
    j = len(input_arr) - 1
    for i in range(len(arr) - 1, 0, -1):
        if input_arr[i] == "  ":
            for char in range(i, j + 1, 1):
                output.append(input_arr[char])
            j = i
    for i in range(0, j + 1, 1):
        output.append(input_arr[i])
    return output[1:-1]


print(
    reverse_words(
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
