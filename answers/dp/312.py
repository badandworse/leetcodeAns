class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        nums.insert(0,1)
        nums.append(1)
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for le in range(1,length+1):
            for left in range(1,length-le+1+1):
                right=left+le-1
                for k in range(left,right+1):
                    dp[left][right]=max(dp[left][right],nums[left-1]*nums[k]*nums[right+1]+dp[left][k-1]+dp[k+1][right])
        
        return dp[1][length]

mm=Solution()
mm.maxCoins([3,5,1,8])