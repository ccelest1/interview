"""
given array of unique chars
Array arr
string str
implement fxn that finds smallest substr of str with all chars in arr
Return str at base case if it doesn't exist (edge case either if str is empty, shorter than array, or doesn't have arr elements in a row or at all)

implement a sliding window approach
two for loops, one starts at index 0, +1, list end-1 and one starts at index 1 list end-1

"""


def get_shortest_substr(arr, str):
    substr = ""
    for i in range(len(str)):
        for j in range(i, len(str)):
            new_set = set(arr)
            substring_length = j - i + 1
            print(substring_length, len(arr))
            # continue to iterate through str to get substrings where the length is greater than length of arr-1, break if substring length is less than array length
            # if provided array has length of 3, only perform rest of steps with substrings of str that have a min length of 3
            if substring_length < len(arr):
                continue
            # print(f'prior {new_set}')
            # return all potential substrings in str with minimum length of len(arr)
            sub_string = str[i : j + 1]
            print(sub_string)
            # print(sub_string)
            """
            iterate through current stored sub_string
            if iterator (sub_string element) is in new_set, then remove it from set
            """
            for ele in sub_string:
                if ele in new_set:
                    print(new_set)
                    new_set.remove(ele)
            # print(f'this {new_set}')
            """

            """
            if len(new_set) == 0:
                if substr == "" or substring_length < len(substr):
                    print(f"this is {substr}")
                    substr = sub_string
    return substr


print(get_shortest_substr(["x", "y", "z"], "xyyzyzyx"))
