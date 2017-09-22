#%%
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        m=dict()
        n=len(s)
        i=0
        while i<n:
            if s[i] in m:
                m[s[i]].append(i)
            else:
                m[s[i]]=[i]
            i+=1
        maxS=s[0]
        maxcount=1
        for ll in m:
            length=len(m[ll])
            if length>1:
                q=0
                while q<length-1:
                    i=length-1
                    isP=True
                    while i>q:
                        testS=s[m[ll][q]:m[ll][i]+1]
                        mm=len(testS)-1
                        l=0
                        isP=True
                        while l<mm:
                            if testS[mm]!=testS[l]:
                                isP=False
                                break
                            else:
                                l=l+1
                                mm=mm-1
                        if isP:
                            if len(testS)>maxcount:
                                maxS=testS
                                maxcount=len(testS)
                            break
                        i=i-1
                    if isP:
                        break
                    q=q+1
        return maxS

longestPalindrome("babadada")

#%%
m=dict()
len(m.keys())