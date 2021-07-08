class Solution:

    def maxProfit(self, prices):
        maxprofit, minprice = 0, float('inf')
        for price in prices:
            minprice = min(minprice, price)
            profit = price - minprice
            maxprofit = max(maxprofit, profit)
        return maxprofit