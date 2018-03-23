class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right,count={},{},{}
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]]=i
            right[nums[i]]=i
            count[i]=count.get(i,0)+1
        
        degree=max(count.values())
        MAXL=50001
        for x in nums:
            if count[x]==degree:
                MAXL=right[x]-left[x]+1 if right[x]-left[x]+1<MAXL else MAXL
        return MAXL


mm=Solution()
mm.findShortestSubArray([1,2,2,3,1])