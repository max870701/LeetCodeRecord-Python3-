function productExceptSelf(nums: number[]): number[] {
    var res: number[] = new Array(nums.length).fill(1)

    // Update Prefix and the result array
    for (let i = 1; i < nums.length; i++) {
        res[i] = res[i-1] * nums[i-1]
    }

    // Update Postfix and the result array
    var postfix: number = 1
    for (let j = nums.length - 2; j >= 0; j--) {
        postfix *= nums[j+1]
        res[j] *= postfix
    }

    return res
};