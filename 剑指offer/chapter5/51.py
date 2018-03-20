#%%
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        copy=[x for x in data]
        count=self.MergeSort(data,copy,0,len(data)-1)
        return count
    
    
    def MergeSort(self,data,copy,start,end):
        if start>=end:
            copy[start]=data[start]
            return 0
        length=(end-start)//2
        left=self.MergeSort(data,copy,start,start+length)
        right=self.MergeSort(data,copy,start+length+1,end)
        
        i=length+start
        j=end
        count=0
        indexCopy=end
        while i>=start and j>=start+length+1:
            if data[i]>data[j]:
                copy[indexCopy]=data[i]
                count+=j-start-length
                i-=1
                indexCopy-=1
            else:
                copy[indexCopy]=data[j]
                indexCopy-=1
                j-=1
        while i>=start:
            copy[indexCopy]=data[i]
            i-=1
            indexCopy-=1
        while j>=start+length+1:
            copy[indexCopy]=data[j]
            indexCopy-=1
            j-=1
        for i in range(len(copy)):
            data[i]=copy[i]
        return left+right+count

mm=Solution()
mm.InversePairs([7,5,6,4])

