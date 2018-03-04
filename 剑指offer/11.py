# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        begin=0
        end=len(rotateArray)-1
        while rotateArray[begin]>=rotateArray[end]:
            if end-begin==1:
                return rotateArray[end]
            mid=begin+int((end-begin)/2)
            if rotateArray[end]==rotateArray[mid]==rotateArray[begin]:
                return self.findMin(rotateArray)
            if rotateArray[mid]>=rotateArray[begin]:
                begin=mid
            elif rotateArray[mid]<=rotateArray[end]:
                end=mid
        

    def findMind(self,rotateArray):
        return min(rotateArray)