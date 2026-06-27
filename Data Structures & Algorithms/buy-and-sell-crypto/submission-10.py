class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0 
        for i in range(len(prices)):
            profit = prices[i] - prices[l]
            maxP = max(profit, maxP)
            if prices[i] < prices[l]:
                l = i
        return maxP