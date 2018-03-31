class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        result=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==False:
                    continue
                result+=1
                self.dfs(grid,i,j,rows,cols)
        return result
    
    def dfs(self,grid,i,j,m,n):
        if i<0 or j<0 or i>=m or j>=n:
            return
        if grid[i][j]==True:
            grid[i][j]=False
            self.dfs(grid,i-1,j,m,n)
            self.dfs(grid,i+1,j,m,n)
            self.dfs(grid,i,j-1,m,n)
            self.dfs(grid,i,j+1,m,n)


mm=Solution()
mm.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])