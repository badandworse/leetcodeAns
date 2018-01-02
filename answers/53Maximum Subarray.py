'''
返回一个list中最大连续子数组的和
本题的关键是如何判断当前数与
之前连续数组有没有必要加在一起,
因此需要让当前数和此前连续数组和+当前数比较
如果当前数更大，则应该舍弃之前的数组，
然后再用较大者比较此时最大和，大的则保留下来
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curS=maxS=nums[0]
        for x in nums[1:]:
            curS=max(x,curS+x)
            maxS=max(maxS,curS)
        return maxS
            