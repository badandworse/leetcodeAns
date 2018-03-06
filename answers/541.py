class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s:
            return ''
        
        resultList=[]
        size=len(s)
        for i in range(0,size,2*k):
            resultList.append(s[i:i+k][::-1]+s[i+k:i+2*k])
        
        return ''.join(resultList)