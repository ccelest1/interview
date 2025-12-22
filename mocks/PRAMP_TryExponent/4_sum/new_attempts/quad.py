from typing import List


def find_array_quadruplet(arr: List[int], s: int) -> List[int]:
    """
    N = len(arr)
    first step - eliminate non possible
    len(N) < 4
    sum(arr) < s
    ! arr
    second step - arr.sort()
    third -
    iterate through array using two pointers
    # why these for iteration
        for i in range(0, N-3)
        for j in range(i+1, N-2)
        r = s - (arr[i] + arr[j])
        # why these for pointers, I thought low = i+1, high = j+1
        low = j + 1
        high = N - 1
        while(low<high):
            if (arr[low]+arr[high]<r):
                low+=1
            elif (arr[high] + arr[low]>r):
                high-=1
            else:
                return [arr[i], arr[j], arr[low], arr[high]]
    using those two numbers then we can find the other two numbers that will sum
    up to remainder to get to s else we return []
    """
    N = len(arr)
    if N < 4 or sum(arr) < s or N == 0:
        return []
    arr.sort()
    for i in range(0, N - 4):
        for j in range(i + 1, N - 3):
            r = s - (arr[i] + arr[j])
            low = j + 1
            high = N - 1
            while low < high:
                high_low = arr[low] + arr[high]
                print(f"this is hl {high_low}")
                print(r)
                if high_low < r:
                    low += 1
                elif high_low > r:
                    high -= 1
                else:
                    quad = [arr[i], arr[j], arr[low], arr[high]]
                    return quad


print(find_array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))
