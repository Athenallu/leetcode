class Solution:
    def find(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    continue
                for num in range(1,10):
                    if self.isvalid(board, i, j, num):
                        board[i][j]=str(num)
                        if self.find(board):
                            return True
                        board[i][j]='.'
                return False
        return True

    def isvalid(self, board, row, col, num):
        for i in range(9):
            if board[i][col]==str(num) or board[row][i]==str(num):
                return False
        
        for i in range((row//3)*3,(row//3)*3+3):
            for j in range((col//3)*3,(col//3)*3+3):
                if board[i][j]==str(num):
                    return False
        return True

        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.find(board)