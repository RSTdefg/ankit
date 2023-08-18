
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)

        for c, p in prerequisites:
            adj_list[c].append(p)

        visited = set()
        def take(course, so_far):
            so_far.add(course)
            visited.add(course)
            res = True
            for p in adj_list[course]:
                if p in so_far:
                    return False
                if p not in visited:
                    res = res and take(p, so_far)
            so_far.remove(course)
            return res
        for i in range(numCourses):
            if i not in visited and not take(i, set()):
                return False
        return True

                    
                



            
