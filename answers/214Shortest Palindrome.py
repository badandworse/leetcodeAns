#%%
#暴力解法:
#先求以首字母开头的最长回文子串
#然后加上其他部分的倒序长度到字符串开头即可
#case 通过119个，还剩一个超时
#最后一个超长例子时无法通过

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s==s[::-1]:
            return s
        maxP=s[0]
        i=1
        maxIndex=1
        while i<len(s)/2+1:
            if s[0:2*i+1]==s[0:2*i+1][::-1]:
                 maxIndex=2*i+1
                 maxP=s[0:2*i+1]
            i+=1
        i=1
        while i<len(s)/2+1:
            slength=i-1-0
            if s[0:2*slength+2]==s[0:2*slength+2][::-1]:
                if len(s[0:2*slength+2])>len(maxP):
                    maxIndex=2*slength+2
                    maxP=s[0:2*slength+2+1]
            i+=1
               
        return s[maxIndex:][::-1]+s

#上面的代码十分冗余，因为符合条件的回文一定是从s[0]开始的
#因此直接从s[0]开始遍历每个s[0]开头的字符串是否满足是回文字符串就可以了
#改良版如下
#但是依然通不过最后一个case的检查
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxIndex=0
        for n in reversed(range(len(s))):
            if s[0:n+1]==s[0:n+1][::-1]:
                maxIndex=n
                break
        return s[maxIndex+1:][::-1]+s


#使用KMP算法思想
#上面暴力解法是求s[0:n]==reversed(s[0:n])最大的n
#这可以看成是s+reversed(s)字符串最大的前缀与后缀字符串相等的字符串
#这里需要加入一个不再s中的字符做为分割字符
#s+'#'+reversed(s)
#这里求next数组是与原来的略不相同，原来的是统计当前索引下前面的字符串的前后缀，即不包括当前这个字符

#%%
class Solution1:
    def shortestPalindrome(self,s):
        reversed_s=s[::-1]
        l=s+'#'+reversed_s
        next_T=[0]*len(l)
        for i in range(1,len(l)):
            j=next_T[i-1]
            while j>0 and l[i]!=l[j]:
                j=next_T[j-1]
            next_T[i]=j+(l[i]==l[j])
        print(next_T)
        return reversed_s[:len(s)-next_T[-1]]+s


testS=Solution1()
testS.shortestPalindrome('abc')