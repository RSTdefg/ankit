
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)
        return self.heap[0]

        
        


