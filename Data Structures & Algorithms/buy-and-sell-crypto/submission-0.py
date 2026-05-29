class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 # buy
        r = 1 # sell
        maxprofit = 0

        while r < n:
           if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
           else:
            l = r
           r += 1
        return maxprofit
        

        