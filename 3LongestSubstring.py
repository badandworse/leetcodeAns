#%%
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        maxcount=0
        i=0
        m=''
        nowcount=0
        while i<len(s):
            temp=s[i]
            if temp in m:
                if nowcount>maxcount:
                    maxcount=nowcount
                nowcount=1
                m=''+temp
            else:
                nowcount+=1
                m=m+temp
            i+=1
        if nowcount>maxcount:
            maxcount=nowcount
        return maxcount

print(lengthOfLongestSubstring("dvdf"))