# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size<=0 or len(num)<size:
            return
        start=0
        length=len(num)
        tempList=[]
        results=[]
        while start<length-size:
            if not tempList:
                tempList=[x for x in num[:size]]
            else:
                del tempList[0]
                tempList.append(num[start+size-1])
            results.append(max(tempList))
            start+=1
        return results

mm=Solution()
mm.maxInWindows([2,3,4,2,6,2,5,1],3)