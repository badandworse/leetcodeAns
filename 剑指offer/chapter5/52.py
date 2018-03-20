# -*- coding:utf-8 -*-
#%%
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        start=self.getFirst(data,k,0,len(data)-1)
        end=self.getLast(data,k,0,len(data)-1)
        
        return end-start+1 if start>-1 else 0
    
    
    def getFirst(self,data,k,start,end):
        if start>end:
            return -1
        
        middle=(start+end)//2
        middleData=data[middle]
        if middleData==k:
            if (middle>0 and data[middle-1]!=k) or middle==0:
                return middle
            else:
                end=middle-1
        elif middleData>k:
            end=middle-1
        else:
            start=middle+1
        return self.getFirst(data,k,start,end)
    
    
    def getLast(self,data,k,start,end):
        if start>end:
            return -1
        middle=(start+end)//2
        middleData=data[middle]
        if middleData==k:
            if (middle<len(data)-1 and data[middle+1]!=k ) or middle==len(data)-1:
                return middle
            else:
                start=middle+1
        elif middleData<k:
            start=middle+1
        else:
            end=middle-1
        return self.getLast(data,k,start,end)


mm=Solution()
mm.GetNumberOfK([1,2,3,3,3,3],3)