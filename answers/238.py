class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return 0
        
        zerosIndex=-1
        allT=1
        length=len(nums)
        for i in range(length):
            if nums[i]==0:
                if zerosIndex>-1:
                    return [0]*length
                zerosIndex=i
            else:
                allT*=nums[i]
        if zerosIndex>-1:
            results=[0]*length
            results[zerosIndex]=allT
            return results
        for j in range(length):
            nums[j]=int(allT/nums[j])
        return nums