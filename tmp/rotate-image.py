
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        C = len(matrix)
        def rotateLayer(i):
            for j in range(i, len(matrix)-i-1):
                matrix[i][j], matrix[j][C-i-1], matrix[C-i-1][C-j-1],matrix[C-j-1][i] = matrix[C-j-1][i] , matrix[i][j], matrix[j][C-i-1], matrix[C-i-1][C-j-1]  
        for n in range(C//2):
            rotateLayer(n)
        

        
