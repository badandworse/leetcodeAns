class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp=[[1,1] for i in range(len(nums))]
        Nmax=1
        for j in range(1,len(nums)):
            maxP=0
            n=1
            for i in range(0,j):
                if nums[j]>nums[i]:
                    if maxP<dp[i][0]+1:
                        maxP=dp[i][0]+1
                        n=dp[i][1]
                    elif maxP==dp[i][0]+1:
                        n+=dp[i][1]
            dp[j][0]=maxP+1
            dp[j][1]=n
            Nmax=max(dp[j][0],Nmax)
        result=0
        for i in dp:
            if i[0]==Nmax:
                result+=i[1]
                
        return result
                