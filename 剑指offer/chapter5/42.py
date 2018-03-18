# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        maxS=curS=array[0]
        for i in array[1:]:
            curS=max(i,curS+i)
            maxS=max(maxS,curS)
        return maxS