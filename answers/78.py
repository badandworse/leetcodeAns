class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for i in nums:
            theList=[]
            for mlist in results:
                theList.append(mlist+[i])
            for ll in theList:
                results.append(ll)
        
        return results