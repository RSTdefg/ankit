
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = collections.deque()
        l, r = 0, 0
        maxi = []
        while r < len(nums):
            while r - l < k:
                while heap and heap[-1] < nums[r]:
                    heap.pop()
                heap.append(nums[r])
                r += 1
            cur_max = heap[0]
            maxi.append(cur_max)
            if heap[0] == nums[l]:
                heap.popleft()
            l += 1
        return maxi

            
            


