
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        employees = [0] * n

        def go(i, sofar):
            if len(requests) - i < max(map(abs, employees)):
                return -1
            if len(requests) == i:
                return sofar
            res = 0
            res = max(res, go(i+1, sofar))
            source, dest = requests[i][0], requests[i][1]
            employees[source] -= 1
            employees[dest] += 1
            res = max(res, go(i+1, sofar+1))
            employees[source] += 1
            employees[dest] -= 1
            return res
        
        return go(0, 0)

            
            
                    
