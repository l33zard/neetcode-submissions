class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0 
        for r in range(1, len(prices)):
            price = prices[r] - prices[l]
            maxP = max(maxP, price)
            if prices[r] < prices[l]:
                l = r
        return maxP