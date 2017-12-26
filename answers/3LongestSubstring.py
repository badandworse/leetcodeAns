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



#python3版本:
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        m=s[0]
        i=1
        longStr=m
        while i<len(s):
            place=m.find(s[i])
            if place>-1:
                if len(m)>len(longStr):
                    longStr=m
                m=m[place+1:]+s[i]
            else:
                m+=s[i]
            i+=1
        
        return len(m) if len(m)>len(longStr) else len(longStr)


#进一步优化
'''
利用hashmap，加已经使用过的str存入
这样在后续的时候只解查看char是否已经在hashmap中
'''