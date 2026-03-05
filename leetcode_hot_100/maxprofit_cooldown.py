class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        hold = -prices[0]
        sell = 0
        freeze = 0

        for i in range(1, len(prices)):
            prev_hold = hold
            prev_sell = sell
            prev_freeze = freeze

            hold = max(prev_hold, prev_freeze - prices[i])
            sell = max(prev_sell, prev_hold + prices[i])
            freeze = max(prev_freeze, prev_sell)

        return sell