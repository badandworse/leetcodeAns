class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 
        reS=s[::-1]
        length=len(s)
        dp=[[0 for i in range(length+1)] for j in range(length+1)]
        for i in range(length):
            for j in range(length):
                if s[i]==reS[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]