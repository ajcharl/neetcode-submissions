class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] >= prices[i]:
                    result = max(result, prices[j] - prices[i])
                else:
                    continue

        return result