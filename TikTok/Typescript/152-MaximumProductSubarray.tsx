function maxProduct(nums: number[]): number {
    var ans: number = nums[0]
    var curMax: number = nums[0]
    var curMin: number = nums[0]

    for (let i = 1; i < nums.length; i++) {
        var n: number = nums[i]
        var tmp: number = curMax * n
        curMax = Math.max(n, tmp, curMin * n)
        curMin = Math.min(n, tmp, curMin * n)
        ans = Math.max(ans, curMax)
    }

    return ans
};