class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z=bin(x^y).replace('0b','')
        result=0
        for i in z:
            if i=='1':
                result+=1
        return result
