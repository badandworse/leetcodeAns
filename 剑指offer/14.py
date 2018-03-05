'''
剪绳子
'''
#%%
class Solution:
    def cutRope(self,length):
        if length<2:
            return 0
        if length==2:
            return 1
        if length==3:
            return 2
        products=[0]*(length+1)
        products[1]=1
        products[2]=2
        products[3]=3
        for i in range(4,length+1):
            Nmax=0
            j=1
            while j<=(i/2):
                nowD=products[i-j]*products[j]
                if nowD>Nmax:
                    Nmax=nowD
                j+=1
            products[i]=Nmax
        return products[length]
#%%
mm=Solution()
mm.cutRope(4)