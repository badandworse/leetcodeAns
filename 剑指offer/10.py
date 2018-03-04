'''
斐波拉契
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n<=2:
            return 1
        f1,f2=1,1
        for i in range(3,n+1):
            f1,f2=f2,f1+f2
        return f2