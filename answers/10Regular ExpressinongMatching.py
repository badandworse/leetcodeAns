#%%
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0:
            return True if len(s)==0 else False
        if p[0]=='*':
            return False
        if '*' not in p  and '.' not in p:
            return s==p
        if '*' not in p:
            self.checkdotRe(s,p)
        if '.*' in p:
            if !s[:p.find('.*')]==p[:p.find('.*')]:
                return False
            s=s[p.find('.*')+1:]
            p=p[p.find('.*')+2:]
            if len(p)==0:
                return True
            else if
            
        if '*' in p:
            while p.find('*')>=0 and len(s)>0:
                p1=p[:p.find('*')-1]
                s1=s[:p.find('*')-1]
                if self.checkdotRe(s1,p1)==False:
                    return False
                else:
                    s=s[p.find('*')-1:]
                    if len(s)==0:
                        break
                    while s[0]==p[p.find('*')-1]:
                        s=s[1:]
                        if len(s)==0:
                            break
                    p=p[p.find('*')+1:]
            return True if len(s)==0 else s==p

    def checkdotRe(self,s,p):
        while p.find('.')>=0:
            if s[:p.find('.')]!=p[:p.find('.')]:
                return False
            else:
                p=p[p.find('.')+1:]
                s=s[p.find('.')+1:]
        return s==p


mm=Solution()
mm.isMatch("a", "ab*a*c*a")

's.*da'.find('.*')

