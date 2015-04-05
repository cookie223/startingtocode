class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        result = 0
        if not prices: return result
        lowest = prices[0]
        for each in prices[1:]:
            result = max(result, each - lowest)
            lowest = min(each, lowest)
        return result