class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = [s[0]]
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for c in s[1:]:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0