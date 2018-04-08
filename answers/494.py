'''
Target Sum
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        暴力破解
        """
        if not nums:
            return 0
        self.result=0
        self.dfs(nums[1:],S-nums[0])
        self.dfs(nums[1:],S+nums[0])
        return self.result
    
    def dfs(self,nums,target):
        if not nums:
            if target==0:
                self.result+=1
            return
        self.dfs(nums[1:],target-nums[0])
        self.dfs(nums[1:],target+nums[0]) 
    
        
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        动态规划
        """
        dp=[0 for _ in range(2001)]
        if nums[0]==0:
            dp[1000]=2
        else:
            dp[nums[0]+1000]=1
            dp[-nums[0]+1000]=1
        for i in range(1,len(nums)):
            next=[0 for _ in range(2001)]
            for sum in range(-1000,1001):
                if dp[sum+1000]>0:
                    next[sum+nums[i]+1000]+=dp[sum+1000]
                    next[sum-nums[i]+1000]+=dp[sum+1000]
            dp=next
        return 0 if S>1000 else dp[S+1000]