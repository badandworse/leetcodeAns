# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        mdict={}
        for i in numbers:
            if i in mdict:
                mdict[i]+=1
            else:
                mdict[i]=1
        for i,j in mdict.items():
            if j>len(numbers)/2:
                return i
        return 0
