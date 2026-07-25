class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = left+1
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
                right += 1

        return maxProfit