class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        j=0
        i=len(s)-1
        while i>=0 and i>j-1:
            if s[i]==s[j]:
                j=j+1
            else:
                j=0
            i-=1
        return  s[i+1:][::-1]+s[:i+1]
        
