# -*- coding:utf-8 -*-
#%%
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k<0:
            return 
        start=0
        end=len(tinput)-1
        if k>=end+1:
            return tinput
        index=self.partition(tinput,start,end)
        while index!=k-1:
            if index>k-1:
                end=index-1
                index=self.partition(tinput,start,end)
            else:
                start=index+1
                index=self.partition(tinput,start,end)
        results=[]
        for i in range(index+1):
            results.append(tinput[i])
        return results
    
    def partition(self,nums,start,end):
        lo=start+1
        right=end
        mm=nums[start]
        while True:
            while nums[lo]<=mm and lo<end:
                lo+=1
            while nums[right]>mm and right>start :
                right-=1
            if lo>=right:
                break
            nums[lo],nums[right]=nums[right],nums[lo]
        return lo


mm=Solution()
mm.GetLeastNumbers_Solution([1,2,3,4,5,6,7,8],4)