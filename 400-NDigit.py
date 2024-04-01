class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1 - 9 => 9 * 1 digits
        # 10 - 99 => 90 * 2 digits
        # 100 - 999 => 900 * 3 digits
        length = 1
        amount = 9

        while n > length * amount:
            n -= length * amount
            length += 1
            amount *= 10

        start_num = 10 ** (length - 1)
        p, q = n // length, n % length

        if q == 0:
            target_num = start_num + p - 1
        else:
            target_num = (start_num + p) // (10 ** (length - q))
            
        return target_num % 10