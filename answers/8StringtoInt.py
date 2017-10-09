'''
这题的思想很简单，其实就是考虑多种情况
先去掉所有空格，然后再来开始循环遍历，如果遇到‘+’或‘-’
就判定是不是已经有了，如果有则结束循环
没有可以暂时加入
然后判定是不是字符，不是则结束循环
最后在利用try/except 检测是否能正常转换为int，能则判断是否超限
不能则直接返回0
'''


#%%
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        if len(str)==0:
            return 0
        else:
            m=''
            i=0
            while i<len(str):
                if ord(str[i])==43:
                    if m.find(str[i])>=0:
                        break
                elif ord(str[i])==45:
                    if m.find(str[i])>=0:
                        break
                elif ord(str[i])<48 or ord(str[i])>57:
                        break
                m+=str[i]
                i+=1
            try:
                if int(m)>2147483647:
                    return 2147483647
                elif int(m)<-2147483648:
                    return (-2147483648)
                return int(m)
            except ValueError:
                return 0




#%%
test=Solution()
test.myAtoi("-2147483649")
