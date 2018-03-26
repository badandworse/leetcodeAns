class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        list1=nums[:k]
        results=[max(list1)]
        for i in range(k,len(nums)):
            if list1[0]==results[-1]:
                del list1[0]
                list1.append(nums[i])
                results.append(max(list1))
            else:
                del list1[0]
                list1.append(nums[i])
                if nums[i]>results[-1]:
                    results.append(nums[i])
                else:
                    results.append(results[-1])
        return results