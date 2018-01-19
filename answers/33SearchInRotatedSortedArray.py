class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        length=len(nums)
        while i<length:
            if nums[i]==target:
                return i
            i+=1
        return -1