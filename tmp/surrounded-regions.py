
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def alive(i, j):
            board[i][j] = 'A'
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i+di, j+dj
                if 0 < ni < len(board) and 0 < nj < len(board[0]) and board[ni][nj] == 'O':
                    alive(ni, nj)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if x == 0 or x == len(board)-1 or y == 0 or y == len(board[0])-1:
                    if board[x][y] == 'O':
                        alive(x, y)
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] = 'X' if board[x][y] != 'A' else 'O'
        




