"""

    LC Notes -
     Required to sort input array which will take O(n log n)
     Going to keep track of the required count of rooms depending on start, end of meeting periods depending on overlaps/ties
     starts and ends times in separate arrays
     Space is going to be O(n)

"""


def minMeetingRooms(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res


print(minMeetingRooms([[0, 30], [11, 19], [15, 20]]))
#  should be 3

print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
# 2
print(minMeetingRooms([[7, 10], [2, 4]]))
# 1
