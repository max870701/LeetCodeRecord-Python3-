function minSubArrayLen(target: number, nums: number[]): number {
    // O(n) Sliding Window
    var left: number = 0
    var right: number = 0
    var n: number = nums.length
    var ans: number = Infinity
    var tmp: number = 0

    while (right < n) {
        // Expand the window
        tmp += nums[right]
        right++
        // Shrink the window
        while (tmp - nums[left] >= target) {
            tmp -= nums[left]
            left++
        }
        if (tmp >= target) {
            ans = Math.min(ans, right - left)
        }
    }

    return Object.is(ans, Infinity) ? 0 : ans
};