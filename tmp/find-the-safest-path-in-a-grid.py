
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        dist = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]

        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    dist[i][j] = 0
        while q:
            i, j, d = q.popleft()
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj, dist[ni][nj]))
        def good(target):
            q = deque()
            visited = [[0]*len(grid[0]) for _ in range(len(grid))]
            if dist[0][0] >= target:
                q.append((0,0))
                visited[0][0] = 1
            while q:
                i, j = q.popleft()
                if (i,j) == (len(grid)-1,len(grid[0])-1):
                    return True
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not visited[ni][nj] and dist[ni][nj] >= target:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
            return False

        l, r = 0, len(grid)
        while l <= r:
            mid = l + (r-l)//2
            if good(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
