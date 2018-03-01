class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for x in nums:
            self.genRe(x,results)
            
        return results
    
    def genRe(self,x,results):
        length=len(results)
        for q in range(length):
            mlen=len(results[0])
            for i in range(mlen+1):
                results.append(results[0][:i]+[x]+results[0][i:])
            del results[0]