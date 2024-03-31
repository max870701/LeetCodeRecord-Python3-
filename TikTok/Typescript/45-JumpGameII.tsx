function jump(nums: number[]): number {
    var ans: number = 0
    var window_left: number = 0
    var window_right: number = 0

    // Break the loop when the index reaches the last position
    while (window_right < nums.length - 1) {
        var farthest: number = 0
        for (let i = window_left; i <= window_right; i++) {
            farthest = Math.max(farthest, i + nums[i])
        }
        // Update the window left and right
        window_left = window_right + 1
        window_right = farthest
        ans++
    }

    return ans
};