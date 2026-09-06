class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0 
        for i in range(1, len(prices)):
            price = prices[r] - prices[l]
            maxP = max(maxP, price)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP