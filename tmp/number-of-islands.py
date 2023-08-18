
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        def dfs(i, j):
            nonlocal res
            for di, dj in [(0,1), (0,-1),(1,0),(-1,0)]:
                if 0 <= i+di<len(grid) and 0 <= j+dj < len(grid[0]) and not visited[i+di][j+dj]:
                    visited[i+di][j+dj] = True
                    if grid[i+di][j+dj] == '1':
                        fill(i+di, j+dj)
                        res += 1
                    else:
                        dfs(i+di, j + dj)
        def fill(i, j):
            for di, dj in [(0,1), (0,-1),(1,0),(-1,0)]:
                if 0<=i+di<len(grid) and 0 <= j+dj < len(grid[0]) and not visited[i+di][j+dj] and grid[i+di][j+dj] == '1':
                    visited[i+di][j+dj] = True
                    fill(i+di, j+dj) 
        visited[0][0] = True
        if grid[0][0] == '1':
            res = 1
            fill(0, 0)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if not visited[x][y]:
                    dfs(x, y)

        return res


            
