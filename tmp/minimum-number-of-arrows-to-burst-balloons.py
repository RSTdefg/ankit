
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        overlap1 = points[0][1]
        result = 0
        for i in range(1, len(points)):
            if points[i][0] > overlap1:
                result += 1
                overlap1 = points[i][1]
            else:
                overlap1 = min(overlap1,  points[i][1])
        return result + 1

            
            
