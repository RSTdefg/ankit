
class Solution:
    def trap(self, height: List[int]) -> int:
        left2right = [0 for _ in range(len(height))]
        right2left = [0 for _ in range(len(height))]
        mini, result = 0, 0
        for i in range(len(height)):
            mini = max(mini, height[i])
            left2right[i] = mini
        mini = 0
        for i in range(len(height)-1, -1, -1):
            mini = max(mini, height[i])
            right2left[i] = mini
        print(right2left, left2right)
        for i in range(len(height)):
            result += min(left2right[i], right2left[i])-height[i]
        return result

        

