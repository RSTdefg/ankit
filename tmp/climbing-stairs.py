
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        i = 0
        while i < n:
            one, two = two + one, one
            i+=1
        return two
