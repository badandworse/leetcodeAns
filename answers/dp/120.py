class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length=len(triangle)
        dp=[x for x in triangle[-1]]
        for i in range(length-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        return dp[0]
    