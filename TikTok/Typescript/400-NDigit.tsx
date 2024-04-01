function findNthDigit(n: number): number {
    // 1-9 => 9 * 1 digits
    // 10-99 => 90 * 2 digits
    // 100-999 => 900 * 3 digits
    let digits = 1, count = 9

    while (n > digits * count) {
        n -= digits * count
        digits++
        count *= 10
    }

    const start_num = 10 ** (digits - 1)
    const q = Math.floor(n / digits), r = n % digits
    let target_num: number

    if (r === 0) {
        target_num = start_num + q - 1
    } else {
        target_num = Math.floor((start_num + q) / (10 ** (digits - r)))
    }
    return target_num % 10
};