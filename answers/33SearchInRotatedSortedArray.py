#%%
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

    if len(nums)==0:
            return -1
        begin=0
        end=len(nums)-1
        Nmin=0
        while begin<=end:
            mid=begin+int((end-begin)/2)
            if nums[mid]<nums[Nmin]:
                Nmin=mid
                end=mid-1
            else:
                begin=mid+1
        
        
        if nums[Nmin]==target:
            return Nmin
        i=0
        end=Nmin-1 if Nmin>0 else len(nums)-1
        tIndex=self.findT(nums,i,end,target)
        if tIndex>-1:
            return tIndex
        i=Nmin+1
        end=len(nums)-1 if Nmin>0 else-1
        return self.findT(nums,i,end,target)
    
    def findT(self,nums,i,end,target):
        while i<=end:
            mid=i+int((end-i)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                i=mid+1
        
        return -1
#%%
msss=Solution()
aList=[3,1]
msss.BinarySearch(aList,1)