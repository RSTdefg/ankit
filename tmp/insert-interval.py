
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if end < newInterval[0]:
                result.append([start, end])
            elif start > newInterval[1]:
                result.append(newInterval)
                result += intervals[i:]
                return result
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        result.append(newInterval)
        return result 

