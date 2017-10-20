#%%
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if self.checkisOver(x):
            return 0
        if x>0:
            return int(str(x)[::-1]) if not self.checkisOver(int(str(x)[::-1])) else 0
        else:
            return -1*int(str(x)[1::][::-1]) if not self.checkisOver(-int(str(x)[::-1])) else 0
    
    def checkisOver(self,x):
        if x==0 or x>2147483647 or x<-2147483648:
            return True
        else:
            return False
