import sys

class Solution:
    def maxDiffSubArrays(self,nums):
        if not nums:
            return 0
        size=len(nums)
        leftMax,leftMin=[0 for _ in range(size)],[0 for i in range(size)]
        rightMax,rightMin=[0 for _ in range(size)],[0 for i in range(size)]
        maxRes,minRes,sum,minSum,maxSum=-float('inf')-1,float('inf'),0,0,0
        for i in range(size):
            sum+=nums[i]
            #如果i左边只有大于0的数，那minSum始终是0
            #对于maxSum也是始终要排除<0的数
            maxRes=max(maxRes,sum-minSum)
            minSum=min(minSum,sum)
            leftMax[i]=maxRes
            minRes=min(minRes,sum-maxSum)
            maxSum=max(maxSum,sum)
            leftMin[i]=minRes

        maxRes,minRes,sum,minSum,maxSum=-float('inf')-1,float('inf'),0,0,0
        
        for i in range(size - 1, -1, -1):
            sum += nums[i]
            maxRes = max(maxRes, sum - minSum)
            minSum = min(minSum, sum)
            rightMax[i] = maxRes
            minRes = min(minRes, sum - maxSum)
            maxSum = max(maxSum, sum)
            rightMin[i] = minRes
        
        result=-float('inf')-1
        for i in range(size-1):
            result=max(result,abs(leftMax[i]-rightMin[i+1]),abs(leftMin[i]-rightMax[i+1]))
        return result