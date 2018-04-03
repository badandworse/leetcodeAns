class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lessmid=0
        moremid=0
        start=1
        end=len(nums)
        mid=(start+end)/2
        while True:
            for i in nums:
                if i<=mid:
                    lessmid+=1
                else:
                    moremid+=1
            
            if lessmid>int(mid):
                if int(mid)-1<=start<=int(mid):
                    return int(mid)
                end=mid
                mid=(start+end)/2
            else:
                if mid<=end<=mid+1:
                    return int(mid)
                start=mid+1
                mid=(start+end)/2

mm=Solution()
mm.findDuplicate([1,1,2])