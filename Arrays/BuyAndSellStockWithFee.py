class Solution:

    def maxProfit(self, prices, fee: int) -> int:
        i = 1
        res = float('-inf')

        def get_profit(prices):
            if not prices:
                return 0
            if len(prices) == 1:
                return 0
            max_profit = float('-inf')
            min_price = float('inf')
            for price in prices:
                min_price = min(price, min_price)
                profit = (price - min_price) - fee
                max_profit = max(profit, max_profit)
            return max_profit

        while i <= len(prices):
            temp = get_profit(prices[:i]) + get_profit(prices[i:])
            res = max(res, temp)
            i+=1
        return res

obj = Solution()
#print(obj.maxProfit([1,3,2,8,4,9], 2))
#print(obj.maxProfit([1,3,7,5,10,3], 3))
#print(obj.maxProfit([1, 5, 9], 2))
print(obj.maxProfit([1,4,6,2,8,3,10,14], 3))

