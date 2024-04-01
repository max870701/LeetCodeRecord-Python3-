// Two Pointers
function minMeetingRooms(intervals: number[][]): number {
    const startTimes = intervals.map(interval => interval[0]).sort((a, b) => a - b)
    const endTimes = intervals.map(interval => interval[1]).sort((a, b) => a - b)

    let res = 0, count = 0, s = 0, e = 0

    while (s < intervals.length) {
        if (startTimes[s] < endTimes[e]) {
            count++
            s++
        } else {
            count--
            e++
        }
        res = Math.max(res, count)
    }

    return res
};