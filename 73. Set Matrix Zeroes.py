class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    pos.append([i,j])
        for p in pos:
            matrix[p[0]]=[0]*len(matrix[0])
            for i in range(len(matrix)):
                matrix[i][p[1]]=0