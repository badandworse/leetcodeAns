#%%
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows==1:
            return s
        else:
            i=1
            m=''
            while i<=numRows:
                m+=self.getStr(s,numRows,i)
                i+=1
            return m
    
    def getStr(self,s,n,i):
        m=s[i-1]
        q1=2*n-2*i
        q2=2*(i-1)
        p=i-1
        while p<=len(s)-1:
            if q1>0:
                p+=q1
                if p<=len(s)-1:
                    m+=s[p]
                else:
                    return m
            if q2>0:
                p+=q2
                if p<=len(s)-1:
                    m+=s[p]
                else:
                    return m
        return m            

#%%
test=Solution()
testStr="AB"

test.convert(testStr,1)
int('123'[::-1])
'123'[1::]
9646324351 
2147483647
1534236469
abs(-1)
