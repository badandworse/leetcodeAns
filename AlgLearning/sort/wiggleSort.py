#%%
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        if not nums or len(nums)<=1:
            return 
        nums.sort()
        i=1
        j=len(nums)-1
        while i<j :
            nums[i],nums[j]=nums[j],nums[i]
            i+=2
            j-=2

ll=[3,5,2,1,6,4]
mm=Solution()
mm.wiggleSort(ll)
ll