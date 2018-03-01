class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastZerosIndex=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastZerosIndex]=nums[i]
                lastZerosIndex+=1
        for i in range(lastZerosIndex,len(nums)):
            nums[i]=0