class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<=0 or m<=0:
            return 
        listN=[i for i in range(n)]
        countZeros=0
        start=0
        while countZeros!=n-1:
            index=(start+m-1)%n
            while listN[index]==-1:
                index+=1
                if index==n:
                    index=0
            listN[index]=-1
            start=index+1
            countZeros+=1
        for i in range(n):
            if listN[i]!=-1:
                return i

from collections import defaultdict