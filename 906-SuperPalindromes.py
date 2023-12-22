class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        self.l_bound, self.r_bound = int(left), int(right)
        sqrt_bound = int(math.sqrt(self.r_bound))

        seed = 1
        num = 0
        ans = 0

        while num < sqrt_bound: # An odd palindrome is in the sqrt boundary
            num = self.getEvenPalindrome(seed)
            if self.check(num * num):
                ans += 1

            num = self.getOddPalindrome(seed)
            if self.check(num * num):
                ans += 1
            
            seed += 1
            
        return ans
    
    def getEvenPalindrome(self, seed):
        res = seed
        while seed != 0:
            res = (res * 10) + (seed % 10)
            seed //= 10
        return res

    def getOddPalindrome(self, seed):
        res = seed
        seed //= 10
        while seed != 0:
            res = (res * 10) + (seed % 10)
            seed //= 10
        return res

    def check(self, num):
        return (num >= self.l_bound) and (num <= self.r_bound) and (self.isPalindrome(num))

    def isPalindrome(self, num):
        # num    : 12321
        # offset : 10000
        offset = 1
        while num // offset >= 10:
            offset *= 10
        while num != 0:
            if (num // offset) != (num % 10): return False
            num = (num % offset) // 10
            offset /= 100
        return True
    

class Solution2():
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002, 10000001, 10011001, 10100101, 10111101, 11000011, 11011011, 11100111, 11111111, 20000002, 100000001, 100010001, 100020001, 100101001, 100111001, 100121001, 101000101, 101010101, 101020101, 101101101, 101111101, 110000011, 110010011, 110020011, 110101011, 110111011, 111000111, 111010111, 111101111, 111111111, 200000002, 200010002]
        return len([i for i in l if (math.sqrt(int(left)) <= i <= math.sqrt(int(right)))])