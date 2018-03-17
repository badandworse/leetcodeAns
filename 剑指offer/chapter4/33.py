# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.isOK(sequence)
    
    def isOK(self,sequence):
        if not sequence:
            return True
        root=sequence[-1]
        i=0
        leftList=[]
        rightList=[]
        while i<len(sequence)-1:
            if sequence[i]>root:
                break
            leftList.append(sequence[i])
            i+=1
        j=i+1
        while j<len(sequence)-1:
            if sequence[j]<root:
                return False
            rightList.append(sequence[j])
            j+=1
        return self.isOK(leftList) and self.isOK(rightList)