# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length=len(numbers)
        if not numbers or length<=1:
            return False
        i=0
        while i<length:
            while numbers[i]!=i:
                if numbers[numbers[i]]==numbers[i]:
                    duplication[0]=numbers[i]
                    return True
                else:
                    numbers[numbers[i]],numbers[i]=numbers[i],numbers[numbers[i]]
            i+=1
        return False


mm=Solution()
mm.duplicate([2,1,3,1,4],[-1])