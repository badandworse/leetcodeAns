class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        height=len(matrix)
        width=len(matrix[0])
        for m in range(height):
            for n in range(m):
                matrix[m][n],matrix[n][m]=matrix[n][m],matrix[m][n]
        
        for i in range(height):
            for j in range(width//2):
                matrix[i][j],matrix[i][width-1-j]=matrix[i][width-1-j],matrix[i][j]