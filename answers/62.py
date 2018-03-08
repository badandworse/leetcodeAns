'''
Unique Paths
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        method=[[0 for i in range(n)] for j in range(m)]
        #first row or col both has only one way
        for i in range(m):
            method[i][0]=1
        for i in range(n):
            method[0][i]=1
        
        for j in range(1,m):
            for q in range(1,n):
                method[j][q]=method[j-1][q]+method[j][q-1]
        return method[m-1][n-1]