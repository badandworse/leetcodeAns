class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length=len(A)
        if length<3:
            return 0
        p=0
        q=1
        nowLess=A[q]-A[p]
        resultsL=[]
        nowT=1
        for i in range(2,length):
            if A[i]-A[q]==nowLess:
                q=i
                nowT=q-p+1
            else:
                if nowT>=3:
                    resultsL.append(nowT)
                nowLess=A[i]-A[q]
                p=q
                q=i
                nowT=q-p+1
            if nowT>=3:
                resultsL.append(nowT)
        sum=0
        for i in resultsL:
            sum+=(i-1)*(i-2)/2
        return sum

m=Solution()
m.numberOfArithmeticSlices([1,2,3,4])