
class Solution:
    def isValid(self, s: str) -> bool:
        m = {'{':'}', '(':')', '[':']'}
        stack = []
        for c in s:
            if c in m:
                stack.append(m[c])
            else:
                if not stack or c != stack[-1]:
                    return False
                stack.pop()
        return stack == []
            


