
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
        for k in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    ti, tj = (k // 3)*3, (k % 3) * 3
                    if board[i+ti][j+tj] == '.':
                        continue
                    if board[i+ti][j+tj] in s:
                        return False
                    s.add(board[i+ti][j+tj])
        return True



