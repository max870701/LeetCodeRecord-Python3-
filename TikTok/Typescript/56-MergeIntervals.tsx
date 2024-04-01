function merge(intervals: number[][]): number[][] {
    // Sort the interval by the order of the start position
    // O(nlogn)
    intervals.sort((a, b) => a[0] - b[0])
    var ans: number[][] = [intervals[0]]

    // Iterate the intervals array and merge overlapped intervals
    for (let i = 1; i < intervals.length; i++) {
        var prevEnd: number = ans[ans.length - 1][1]
        var [curStart, curEnd] = intervals[i]
        if (curStart <= prevEnd) {
            ans[ans.length - 1][1] = Math.max(prevEnd, curEnd)
        } else {
            ans.push([curStart, curEnd])
        }
    }
    return ans
};