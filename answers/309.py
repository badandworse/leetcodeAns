class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=-float('inf')
        prebuy=0
        sell=0
        presell=0
        for i in prices:
            prebuy=buy
            buy=max(presell-i,prebuy)
            presell=sell
            sell=max(prebuy+i,presell)
        return sell