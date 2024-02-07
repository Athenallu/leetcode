from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        res=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    res+=1
                    self.changenb(grid, i, j, q)
                    while q:
                        m, n = q.popleft()
                        self.changenb(grid, m, n, q)
        return res

    def changenb(self, grid, i, j, q):
        row=len(grid)
        col=len(grid[0])
        grid[i][j]='0'
        if i>0 and grid[i-1][j]=='1':
            q.append((i-1,j))
            grid[i-1][j]='0'
        if i<row-1 and grid[i+1][j]=='1':
            q.append((i+1,j))
            grid[i+1][j]='0'
        if j>0 and grid[i][j-1]=='1':
            q.append((i,j-1))
            grid[i][j-1]='0'
        if j<col-1 and grid[i][j+1]=='1':
            q.append((i,j+1))
            grid[i][j+1]='0'