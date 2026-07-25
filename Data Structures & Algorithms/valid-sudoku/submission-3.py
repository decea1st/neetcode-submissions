class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in board:
            rowNums = []
            for j in i:
                if j != ".": rowNums.append(j)
            if len(set(rowNums)) != len(rowNums): return False

        for i in range(9):
            colNums = []
            for j in range(9):
                if board[j][i] != ".": colNums.append(board[j][i])
            if len(set(colNums)) != len(colNums): return False

        for sub in range(9):
            subNums = []
            for i in range(3):
                for j in range(3):
                    row = i + ((sub // 3)*3)
                    col = j + ((sub%3)*3)
                    if board[row][col] != ".": subNums.append(board[row][col])
            if len(set(subNums)) != len(subNums): return False

        return True

board=[[".",".",".",".","5",".",".","1","."],
       [".","4",".","3",".",".",".",".","."],
       [".",".",".",".",".","3",".",".","1"],
       ["8",".",".",".",".",".",".","2","."],
       [".",".","2",".","7",".",".",".","."],
       [".","1","5",".",".",".",".",".","."],
       [".",".",".",".",".","2",".",".","."],
       [".","2",".","9",".",".",".",".","."],
       [".",".","4",".",".",".",".",".","."]]