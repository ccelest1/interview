"""
two inputs: limit = target, arr = array of item weights
given two elements in an array find elements = limit
ouput: [i,j] i>jj
edge case: if pair doesn't exist, return empty array
establish hash map called dic
iterate through arr using enumerate (to get the number and index)
BASICALLY 2 SUM
""" ""

# 2 sum
def get_indices_of_item_wights(arr, limit):
    dic = {}
    for i, num in enumerate(arr):
        if num in dic:
            if dic[num] > i:
                # returning index of the number that is the remainder to get to target
                # as well as the index of the current number of the array iteration
                return [dic[num], i]
            else:
                return [i, dic[num]]
        else:
            # at beginning, store the target remainder with index as value
            dic[limit - num] = i
    return []


# O(n) space complexity - map as aux space
# O(n) time complexity - going through array once and hash function with minimal collisions
