class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        diff = 0
        max_profit = 0

        for curr_price in prices[1:]:
            diff = curr_price - min_price

            if diff < 0:
                min_price = curr_price
            
                

            max_profit = max(diff, max_profit)
        
        return max_profit