
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_graph = [[0]*n for _ in range(n)]

        for a, b in roads:
            adj_graph[a][b] = 1
            adj_graph[b][a] = 1
        
        rank = [0]*n
        for i in range(n):
            rank[i] = sum(adj_graph[i])
        maxi = 0
        for i in range(n):
            for j in range(i+1, n):
                addi = adj_graph[i][j]
                maxi = max(maxi, rank[i]+rank[j]-addi)
        return maxi
        



