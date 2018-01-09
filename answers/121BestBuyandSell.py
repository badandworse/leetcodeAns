'''
本题暴力解法很简单，直接嵌套循环即可
但时间复杂度会是O(N**2)
简单解法是单词循环，如果当前购买价格比当前最低购买价小，
则用当前价格替代最低价格继续循环
如果当前价格-最低价格>最大利润，则替换之
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<1:
            return 0
        maxP=0
        nowB=prices[0]
        for i in prices[1:]:
            if i<nowB:
                nowB=i
                continue
            nowP=i-nowB
            if nowP>maxP:
                maxP=nowP
        return maxP
            