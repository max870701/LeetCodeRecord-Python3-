class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            s = people[l] if l == r else people[l] + people[r]
            if s > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            ans += 1

        return ans
    
class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l <= r:
            s = people[l] if l == r else people[l] + people[r]
            if s <= limit:
                l += 1
            r -= 1
            ans += 1

        return ans