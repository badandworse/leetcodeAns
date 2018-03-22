# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers)<5:
            return False
        
        numbers.sort()
        zerosCount=0
        for i in numbers:
            if i==0:
                zerosCount+=1
        start=zerosCount
        big=start+1
        numberNeed=0
        while big<len(numbers):
            if numbers[start]==numbers[big]:
                return False
            numberNeed+=numbers[big]-numbers[start]-1
            start=big
            big+=1
        return numberNeed<=zerosCount