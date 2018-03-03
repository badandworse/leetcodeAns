class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        results=[0]
        for i in range(1,num+1):
            m=int(i/2)
            n=i%2
            results.append(results[m]+n)
        return results