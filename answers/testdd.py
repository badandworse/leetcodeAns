class Solution:
    
    def paint(self,m,n):
        if m<3 or n<1:
            return None
        if n<3:
            return self.compute(m,2)
    
        res=m*(m-1)**(n-1)-paint(m,n-1)
        return res

    def compute(self,n,m):
        return self.factorial(n)/self.factorial(n-m)


    def factorial(self,n):
        if n==1:
            return 1
        return n*self.factorial(n-1)


mm=Solution()
mm.paint(5,5)