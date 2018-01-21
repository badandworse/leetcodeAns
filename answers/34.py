#%%
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        begin=0
        end=len(nums)-1
        result=[-1,-1]
        self.findT(nums,begin,end,result,target)
        return result
    
    def findT(self,nums,begin,end,resultList,target):
        if begin>end:
            return
        mid=begin+int((end-begin)/2)
        if nums[mid]>target:
            self.findT(nums,begin,mid-1,resultList,target)
        elif nums[mid]<target:
            self.findT(nums,mid+1,end,resultList,target)
        else:
            if sum(resultList)==-2:
                resultList[0]=mid
                resultList[1]=mid
                self.findT(nums,begin,mid-1,resultList,target)
                self.findT(nums,mid+1,end,resultList,target)
            elif mid>resultList[1]:
                resultList[1]=mid
                self.findT(nums,mid+1,end,resultList,target)
            elif mid<resultList[0]:
                resultList[0]=mid
                self.findT(nums,begin,mid-1,resultList,target)
