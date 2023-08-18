
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, W = len(matrix), len(matrix[0])
        left, right = 0, L*W-1

        while left <= right:
            mid = left + (right-left) // 2
            i, j = mid // W, mid % W

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True

        return False

        
