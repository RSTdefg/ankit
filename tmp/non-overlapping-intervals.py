
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        result = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                prev_end = min(prev_end, end)
                result += 1
            else:
                prev_end = end
        return result




