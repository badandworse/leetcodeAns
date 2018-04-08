#%%
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        if amount in coins:
            return 1
        coins.sort()
        if amount<coins[0]:
            return -1
        dp=[-1 for i in range(amount+1)]
        lessCoins=[x for x in coins if x<=amount]
        for i in lessCoins:
            dp[i]=1
        for i in range(lessCoins[0]+1,amount+1):
            if dp[i]==1:
                continue
            minN=-1
            if i==189:
                print(1)
            for m in lessCoins:
                if m>i:
                    break
                if dp[i-m]!=-1:
                    if minN==-1:
                        minN=dp[i-m]+1
                    else:
                        minN=min(dp[i-m]+1,minN)
            dp[i]=minN
        return dp[amount]


mm=Solution()
mm.coinChange([102,220,186,465,336,107,387,418],495)