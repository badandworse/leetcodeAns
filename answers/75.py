'''
Sort Colors
'''
#%%
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        
        i=0
        end=len(nums)-1
        j=0
        while j<=end:
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            elif nums[j]==2:
                nums[j],nums[end]=nums[end],nums[j]
                end-=1
            else:
                j+=1
                

#%%
m=Solution()
a=[1,2,0]
m.sortColors(a)
a
