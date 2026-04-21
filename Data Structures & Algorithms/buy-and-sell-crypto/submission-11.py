class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for current_price in prices[1:]:
            if current_price < min_price:
                min_price = current_price
            else:
                profit = current_price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit          
