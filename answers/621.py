'''
task scheduler
'''

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        array=[0 for _ in range(26)]
        for task in tasks:
            array[ord(task)-ord('A')]+=1
        array.sort()
        mxn=array[-1]
        maxLength=(mxn-1)*(n+1) +array.count(mxn)
        return max(maxLength,len(tasks))