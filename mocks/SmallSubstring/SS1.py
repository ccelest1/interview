# 2 inputs: array , string
# function 2 inputs -> find a substring possible in str given the characters provided in arr
# if you cant make a substring in str, from characters provided in arr return "" (empty string)
# outputs: empty string (edge case), smallest possible substring

"""
set = {x, y, z}
       01234567
str = "xyyzyzyx"
       i
          j
       xyy

arr=[x,y,z]
 x: [x,z,y], [x,y,z]
 z: [z,y,x], [z,x,y]
 y: [y,x,z], [y,z,x]
"""
# set.join()===str[i:length]
# return output
def get_shortest_unique_substring(arr, str):
    res = ""
    for i in range(len(str)):
        for j in range(i, len(str)):
            new_set = set(arr)
            substring_length = j - i + 1
            if substring_length < len(arr):
                continue
            sub_string = str[i : j + 1]
            for c in sub_string:
                if c in new_set:
                    new_set.remove(c)
            if len(new_set) == 0:
                if res == "" or substring_length < len(res):
                    res = sub_string
    return res


arr = ["x", "y", "z"]
str = "xyyzyzyx"
print(get_shortest_unique_substring(arr, str))

"""
O(n^3) time complexity, O(n) space complexity
time - 3 nested for loops
space - adding to a string as you iterate through given string
"""
