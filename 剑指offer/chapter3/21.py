# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        array1=[]
        array2=[]
        for i in array:
            if i%2==0:
                array2.append(i)
            else:
                array1.append(i)
        return array1+array2