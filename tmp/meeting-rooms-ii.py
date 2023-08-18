
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        heap = []
        intervals.sort()
        heap.append(intervals[0][1])
        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
            
