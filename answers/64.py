class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        height=len(grid)
        width=len(grid[0])
        mm=[[0 for i in range(width)] for j in range(height)]
        mm[0][0]=grid[0][0]
        for i in range(1,height):
            mm[i][0]=mm[i-1][0]+grid[i][0]
        for i in range(1,width):
            mm[0][i]=mm[0][i-1]+grid[0][i]
        
        for m in range(1,height):
            for n in range(1,width):
                mm[m][n]=min(mm[m-1][n],mm[m][n-1])+grid[m][n]
        return mm[height-1][width-1]