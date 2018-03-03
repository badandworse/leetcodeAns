class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1=cost[0] 
        f2=cost[1]
        for i in range(2,len(cost)):
            f1,f2=f2,min(f1,f2)+cost[i]
        return min(f1,f2)