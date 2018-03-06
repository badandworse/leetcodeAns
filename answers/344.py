class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList=list(s)
        i=len(s)-1
        beg=0
        while beg<i:
            strList[beg],strList[i]=strList[i],strList[beg]
            beg+=1
            i-=1
        return ''.join(strList)