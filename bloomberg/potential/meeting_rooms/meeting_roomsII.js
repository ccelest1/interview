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
    let [l, r] = [1, 0]
    let rooms = 0
    let [lsum, rsum] = [starts[0], ends[0]]
    while (l <= starts.length && r <= ends.length) {
        lsum += starts[l]
        rsum += ends[r]
        if (lsum < rsum) {
            rooms += 1
            l += 1
        } else {
            r += 1
        }
    }
    return rooms
}

console.log(meeting_rooms(
    [[0, 30], [5, 10], [15, 20]]
))
//2
console.log(meeting_rooms(
    [[7, 10], [2, 4]]
))
