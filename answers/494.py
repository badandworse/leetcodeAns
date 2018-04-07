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
    
        