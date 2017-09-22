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
            ll=m.find(temp)
            if ll>=0:
                if nowcount>maxcount:
                    maxcount=nowcount
                m=m[ll+1:]+temp
                nowcount=len(m)
            else:
                nowcount+=1
                m=m+temp
            i+=1
        if nowcount>maxcount:
            maxcount=nowcount
        return maxcount

print(lengthOfLongestSubstring("dvdf"))