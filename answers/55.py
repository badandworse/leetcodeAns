'''
55. Jump Game
'''

#%%
class Solution1:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        if nums[0]>len(nums):
            return True
        for i in range(1,nums[0]+1):
            if self.canJump(nums[i:]):
                return True
        return False

#%%
class Solution2:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        mdict={}
        return self.isReach(nums,mdict,0)
    
    def isReach(self,nums,mdict,startIndex):
        if len(nums)==1 or nums[0]>len(nums):
            return True
        if nums[0]==0:
            mdict[startIndex]=False
            return False
        if startIndex in mdict:
            return False
        
        for in range(1,nums[0]+1):
            if self.isReach(nums[i:],mdict,startIndex+i):
                return True
        
        mdict[startIndex]=False
        return False


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)-1
        lastPosition=length
        for i in reversed(range(0,length)):
            if i+nums[i]>=lastPosition:
                lastPosition=i
        return lastPosition==0