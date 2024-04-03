/*
    LC Premium - Meeting Rooms II
    Given array of meeting time intervals that have start and end times, find min number
    of conference rooms required

 */
/**
 * @param {number[][]} arr
 * @return {number}
 */
var minMeetingRooms = function (intervals) {
    let starts = []
    let ends = []
    for (let block in intervals) {
        starts.push(intervals[block][0])
        ends.push(intervals[block][1])
    }
    starts.sort((a, b) => a - b)
    ends.sort((a, b) => a - b)
    let [l, r] = [0, 0]
    let rooms = 0
    let start, end;
    let res = 0;
    while (l <= starts.length && r <= ends.length) {
        start = starts[l]
        end = ends[r]
        if (start < end) {
            l += 1
            rooms += 1
        } else {
            r += 1
            rooms -= 1
        }
        // we want to continue to find max if possible
        res = Math.max(res, rooms)
    }
    return res
}

console.log(minMeetingRooms(
    [[0, 30], [11, 19], [15, 20]]
))
//  should be 3

console.log(minMeetingRooms(
    [[0, 30], [5, 10], [15, 20]]
))
//2
console.log(minMeetingRooms(
    [[7, 10], [2, 4]]
))
// 1
