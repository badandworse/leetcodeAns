#%%
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1=0
        if len(nums)<=1:
            return False
        if len(nums)==2:
            return nums[0]==nums[1]
        for i in nums:
            sum1+=i
        if sum1%2==1:
            return False
        target=sum1//2
        lessTarget=[x for x in nums if x<target]
        lessTarget.sort()
        dp=[0 for _ in range(target+1)]
        dp[0]=1
        for i in range(len(lessTarget)):
            for j in range(target,-1,-1):
                if j-lessTarget[i]>=0:
                    dp[j]=dp[j] or dp[j-lessTarget[i]]
        return dp[-1]==1
