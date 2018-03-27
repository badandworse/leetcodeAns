class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index=abs(nums[i])-1
            nums[index]=-abs(nums[index])
        return [i+1 for i,num in enumerate(nums) if num>0]