class Solution:
    def maxProfit(self, prices) -> int:
        res=0
        cur=prices[0]
        for i in range(1, len(prices)):
            diff=prices[i]-cur
            if diff>0:
                res+=diff
            cur=prices[i]
        return res