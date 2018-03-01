class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length=len(s)
        result=length
        for i in range(1,length-1):
            q=1
            pathNum=min(i,length-i-1)
            while q<=pathNum:
                if self.checkOneTrue(s,i,q):
                    result+=1
                    q+=1
                else:
                    break
            
        for i in range(0,length-1):
            q=0
            pathNum=min(i,length-i-1-1)
            while q<=pathNum:
                if self.checkTwoTrue(s,i,q):
                    result+=1
                    q+=1
                else:
                    break
        return result
    
    def checkOneTrue(self,s,i,q):
        checkS =s[i-q:i+q+1]
        if checkS[::-1]==checkS:
            print(checkS)
            return True
        return False

    def checkTwoTrue(self,s,i,q):
        checkS=s[i-q:i+1+q+1]
        if checkS[::-1]==checkS:
            print(checkS)
            return True
        return False



class Solution2:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        length=len(s)
        result=length
        for i in range(1,length-1):
            q=1
            pathNum=min(i,length-i-1)
            while q<=pathNum:
                if s[i-q:i+q+1]==s[i-q:i+q+1][::-1]:
                    result+=1
                    q+=1
            else:
                break
        
        for i in range(0,length-1):
            q=0
            pathNum=min(i,legnth-i-1-1)
            while q<=pathNum:
                if s[i-q:i+q+1+1]==s[i-q:i+q+1+1][::-1]:
                    result+=1
                    q+=1
            else:
                break
        
        return result


mm=Solution2()
mm.countSubstrings('abc')
