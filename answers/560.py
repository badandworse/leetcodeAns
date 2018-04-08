'''
Subarray Sum Equals K
'''
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        0(n*n)解法
        """
        result=0
        length=len(nums)
        for i in range(length):
            sum1=0
            for j in range(i,length):
                sum1+=nums[j]
                if sum1==k:
                    result+=1
        return result
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        O(n)解法
        """
        mdict={0:1}
        result=0
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1-k in mdict:
                result+=mdict[sum1-k]
            if sum1 in mdict:
                mdict[sum1]+=1
            else:
                mdict[sum1]=1
        return result