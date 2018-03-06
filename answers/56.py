# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals.sort(key=lambda x:x.start)
        
        merges=[]
        for i in intervals:
            if not merges or merges[-1].end<i.start:
                merges.append(i)
            else:
                merges[-1].end=max(merges[-1].end,i.end)
        
        return merges