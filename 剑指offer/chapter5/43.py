# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        testStr=''
        for i in range(1,n+1):
            testStr+=str(i)
        count=0
        for j in testStr:
            if j=='1':
                count+=1
        return count