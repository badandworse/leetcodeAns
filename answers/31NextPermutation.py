#%%
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        
        if i>=0:
            j=i+1
            while j<len(nums)-1:
                if nums[j+1]<=nums[i]:
                    break
                j+=1
            print(i)
            print(j)
            nums[i],nums[j]=nums[j],nums[i]
        
        nums[i+1:]=nums[i+1:][::-1]
#%%
nums=[5,1,1]
s=Solution()
s.nextPermutation(nums)
nums

