'''
利用的横向扫描，即依次比较相邻的两个字符串

'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        commPre=self.getCommPre(strs[0],strs[1])
        for ss in strs[2:]:
            commPre=self.getCommPre(commPre,ss)
            if commPre=='':
                break
        return commPre
    
    def getCommPre(self,str1,str2):
        length=len(str1) if len(str1)<=len(str2) else len(str2)
        i=0
        s=''
        while i<length:
            if str1[i]==str2[i]:
                s+=str1[i]
            else:
                break
            i+=1
        return s

'''
更好的方法是竖向扫描，即每次比较所有字符串的同位置的字符
这样最差的情况就不用遍历所有的字母，只用遍历所有的字符串前n位
n为最短的那个的长度
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0 or strs[0]=='':
            return ''
        for i in range(0,len(strs[0])):
            for ss in strs[1:]:
                if i==len(ss) or ss[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]
            