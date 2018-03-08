class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        results=[0 for i in range(n+1)]
        i=0
        results[1]=1
        results[0]=1
        for i in range(2,n+1):
            for j in range(0,i):
                results[i]+=results[j]*results[i-j-1]
        
        return results[n]