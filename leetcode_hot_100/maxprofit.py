class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mono_stack = []
        max_profit = 0
        for i in range(len(prices)):
            if not mono_stack or prices[i] < mono_stack[-1]:
                mono_stack.append(prices[i])
            else:
                max_profit = max(prices[i] - mono_stack[-1], max_profit)
        return max_profit