class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        max_prof = 0

        for r in range(len(prices)):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            max_prof = max(max_prof, diff)

        return max_prof