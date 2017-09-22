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


# 以上是错的，经历了几个版本，最初是遍历，但是会因为时间复杂度而导致失败
# 现在最新的版本是，从最右侧向左过度，但这同样有问题，假定的是遇到的第一个回文就是最大的
# 但是问题就是不是的，因为随着向左移动，长度在变小


# 阅读他人博客后，我发现我把事情想复杂了，因为回文字符串就是以中心扩散的，
# 因此可以遍历一下，把每个点当作中心向两边扩散即可
# 但是字符串可能有两个中心，因为回文字符串有可能是偶数，也有可能是基数

#正确答案
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=len(s)
        if length==0:
            return ''
        maxStr=s[0]
        #不需要从最后一个开始，因为到最后一个的话，最大的长度也只可能是1
        for i in range(length-1):
            #这是遍历以当前为基数的
            nowS1=self.getPstring(s,i,i)
            if len(nowS1)>len(maxStr):
                maxStr=nowS1
            nowS2=self.getPstring(s,i,i+1)
            if len(nowS2)>len(maxStr):
                maxStr=nowS2
        return maxStr
    
    def getPstring(self,s,leftbegin,rightbegin):
        l=leftbegin
        i=rightbegin
        while l>=0 and i<len(s) and s[l]==s[i]:
            l-=1
            i+=1
        #list 切片指定终点，是不会包含终点的那个索引的
        return s[l+1:i]

#%%
# 尝试优化:
# 在网上查询的相关优化方法，
# 发现可以略去一些不必要的比较
# 因为已知目前最大字符串，因此新的字符串必须要大于目前已知最大的长度
# 因此可以直接跳过长度不如已知的检验
# 具体操作是，两边的起点各在索引的基础上加上(len(maxStr)-1)/2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=len(s)
        if length==0:
            return ''
        maxStr=s[0]
        #不需要从最后一个开始，因为到最后一个的话，最大的长度也只可能是1
        for i in range(length-1):
            #这是遍历以当前为基数的
            maxlen=len(maxStr)
            beginl=(maxlen-1)/2
            nowS1=self.getPstring(s,i-beginl,i+beginl)
            if len(nowS1)>len(maxStr):
                maxStr=nowS1
            nowS2=self.getPstring(s,i-beginl,i+1+beginl)
            if len(nowS2)>len(maxStr):
                maxStr=nowS2
        return maxStr
    
    def getPstring(self,s,leftbegin,rightbegin):
        l=leftbegin
        i=rightbegin
        str=s[l:i+1]
        if str[::-1]==str:
            while l>=0 and i<len(s) and s[l]==s[i]:
                l-=1
                i+=1
        #list 切片指定终点，是不会包含终点的那个索引的
            return s[l+1:i]
        else:
            return ''