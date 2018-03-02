
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nowNList=[]
        nowSList=['']
        nowLeft=[]
        result=''
        for ll in s:
            if ll.isdigit():
                if len(nowNList)>0 and len(nowNList)>len(nowLeft):
                    nowNList[len(nowNList)-1]=nowNList[len(nowNList)-1]*10+int(ll)
                else:
                    nowNList.append(int(ll))
            elif ll=='[':
                nowLeft.append(ll)
                nowSList.append('')
            elif ll==']':
                num=nowNList.pop()
                ss=nowSList.pop()
                nowLeft.pop()
                if not nowLeft:
                    result+=ss*num
                else:
                    nowSList[len(nowSList)-1]+=ss*num
            else:
                if not nowLeft:
                    result+=ll
                else:
                    nowSList[len(nowSList)-1]+=ll
        
        return result


mm=Solution()
mm.decodeString("100[leetcode]")