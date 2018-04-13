class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for i in range(n+1)]
        dp[1]=1
        for i in range(n+1):
            nowMax=0
            for j in range(1,i):
                nowMax=max(nowMax,dp[j]*dp[i-j])
            dp[i]=nowMax
        return dp[-1]

mm=Solution()
mm.integerBreak(2)