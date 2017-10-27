#%%
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ll=nums1+nums2
        sorted_ll=sorted(ll)
        
        m=len(sorted_ll)
        if m%2==0:
            return (sorted_ll[m/2-1]+sorted_ll[m/2])/2.0
        else:
            return (sorted_ll[m/2])

mm=Solution()

mm.findMedianSortedArrays([1,1],[1,2])

