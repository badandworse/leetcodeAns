#%%
import collections
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k<=0 or len(s)<k:
            return 0
        mdict={}
        length=len(s)
        for i in range(length):
            if s[i] in mdict:
                mdict[s[i]]+=1
            else:
                mdict[s[i]]=1
        
        goodChara=[]
        for j,m in mdict.items():
            if m>=k:
                goodChara.append(j)
        for cha in goodChara:
            del mdict[cha]
        if not mdict:
            return len(s)
        m=[]
        string1=''
        for i in range(length):
            if s[i] in mdict:
                if  string1:
                    m.append(string1)
                    string1=''
            else:
                string1+=s[i]
        if string1 not in m and string1:
            m.append(string1)
        if not m:
            return 0
        else:
            sum1=0
            for ss in m:
                sum1+=self.longestSubstring(ss,k)
        return sum1


