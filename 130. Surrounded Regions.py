class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        row=len(board)
        col=len(board[0])
        if row<=2 or col<=2:
            return

        for i in range(1,row-1):
            for j in range(1, col-1):
                s=set()
                flag=[0]
                q=deque()
                if board[i][j]=='O':
                    self.findnb(board, i, j, s, q, flag)
                    if flag[0]==1:
                        continue
                    while q:
                        m,n=q.popleft()
                        self.findnb(board, m, n, s, q, flag)
                        if flag[0]==1:
                            break
                    if flag[0]==0:
                        for cell in s:
                            board[cell[0]][cell[1]]='X'
        return                

    
    def findnb(self, board, i, j, s, q, flag):
        row=len(board)
        col=len(board[0])
        if (i==1 and board[i-1][j]=='O') or (i==row-2 and board[i+1][j]=='O') or (j==1 and board[i][j-1]=='O') or (j==col-2 and board[i][j+1]=='O'):
            flag[0]=1
            return
        if i>1 and board[i-1][j]=='O' and (i-1,j) not in s:
            s.add((i-1,j))
            q.append((i-1,j))
        if i<row-1 and board[i+1][j]=='O' and (i+1,j) not in s:
            s.add((i+1,j))
            q.append((i+1,j))
        if j>0 and board[i][j-1]=='O' and (i,j-1) not in s:
            s.add((i,j-1))
            q.append((i,j-1))
        if j<col-1 and board[i][j+1]=='O' and (i,j+1) not in s:
            s.add((i,j+1))
            q.append((i,j+1))
        s.add((i,j))
        