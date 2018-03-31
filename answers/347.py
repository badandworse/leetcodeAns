from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mm=Counter(nums)
        mmList=sorted(mm.items(),key=lambda x:x[1],reverse=True)
        results=[]
        for i in range(k):
            results.append(mmList[i][0])
        return results