class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxP = 0
        for r in range(1, len(prices)):
            p = prices[r] - prices[l] 
            maxP = max(p, maxP) 
            if prices[r] < prices[l]:
                l = r
        return maxP