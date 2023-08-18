
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # [9,8,9,1]
        minpq, maxpq = [], []
        for i in range(len(weights)-1):
            heapq.heappush(maxpq, -(weights[i]+weights[i+1]))
            heapq.heappush(minpq, (weights[i]+weights[i+1]))
            while len(maxpq) > k-1:
                heapq.heappop(maxpq)
            while len(minpq) > k-1:
                heapq.heappop(minpq)
        return sum(maxpq)+sum(minpq)
        


