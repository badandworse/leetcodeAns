#%%
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        index=end-k+1
        mindex=self.partion(nums,start,end)
        while mindex!=index and end>start:
            if mindex<index:
                start=mindex+1
            else:
                end=mindex-1
            mindex=self.partion(nums,start,end)
        return nums[mindex]
    
    def partion(self,nums,start,end):
        if start==end:
            return start
        m=nums[start]
        lo=start+1
        right=end
        while True:
            while nums[lo]<m:
                lo+=1
                if lo>=right:
                    break
            while nums[right]>m:
                right-=1
            if lo>=right:
                break
            nums[lo],nums[right]=nums[right],nums[lo]
            lo+=1
            right-=1
        nums[start],nums[right]=nums[right],nums[start]
        return right
