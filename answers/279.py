class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0

        dp=[5 for _ in range(n+1)]
        i=1
        while i*i<=n:
            dp[i*i]=1
            i+=1

        for i in range(1,n+1):
            j=1
            while i+j*j<=n:
                dp[i+j*j]=min(dp[i]+1,dp[i+j*j])
                j+=1
        return dp[-1]
            