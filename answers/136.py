'''
Single Number
'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        mdict={}
        for i in nums:
            if i in mdict:
                del mdict[i]
            else:
                mdict[i]=1
        
        return [x for x in mdict.keys()][0]