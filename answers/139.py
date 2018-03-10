class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length=len(s)
        mm=[False for i in range(length+1)]
        mm[0]=True
        for i in range(1,length+1):
            for ll in range(i):
                if mm[ll] and s[ll:i] in wordDict:
                    mm[i]=True
        return mm[length]