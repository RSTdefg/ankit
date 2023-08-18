
class Solution:
    def minTime(self, n: int, edge_list: List[List[int]], hasApple: List[bool]) -> int:
        edges = set()
        visited = {0}
        adj_list = collections.defaultdict(list)
        for start, end in edge_list:
            adj_list[start].append(end)
            adj_list[end].append(start)
        def dfs(cur, path):
            if hasApple[cur]:
                for p in path:
                    edges.add(p)
            for n in adj_list[cur]:
                if n not in visited:
                    visited.add(n)
                    dfs(n, path+[(cur, n)])
            return
        dfs(0, [])
        return 2*len(edges)
        





