class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        every_nine=[[] for _ in range(9)]
        for i in range(9):
            l=[]
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in every_nine[(i//3)*3+j//3]:
                        return False
                    else:
                        every_nine[(i//3)*3+j//3].append(board[i][j])
                    if board[i][j] in l:
                        return False
                    else:
                        l.append(board[i][j])
        for j in range(9):
            l=[]
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in l:
                        return False
                    else:
                        l.append(board[i][j])
        return True

        