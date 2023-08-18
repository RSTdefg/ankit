
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, u, d = -1, len(matrix[0]), -1, len(matrix)
        di, dj = 0, 1
        i, j = 0, 0
        count = len(matrix) * len(matrix[0])
        result = []
        while count > 0:
            result.append(matrix[i][j])
            count -= 1
            if j + dj == r:
                u += 1
                di, dj = 1, 0
            elif i + di == d:
                r -= 1
                di, dj = 0, -1
            elif j + dj == l:
                d -= 1
                di, dj = -1, 0
            elif i + di == u:
                l += 1
                di, dj = 0, 1
            i, j = i+di, j + dj
        return result
