'''
House Robber
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robnow=0
        notRobnow=0
        for i in range(0,len(nums)):
            courrRob=notRobnow+nums[i]
            notRobnow=max(robnow,notRobnow)
            robnow=courrRob
        return max(notRobnow,robnow)