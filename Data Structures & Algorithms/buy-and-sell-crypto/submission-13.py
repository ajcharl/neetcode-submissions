class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        max_price = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                finalPrice = prices[right] - prices[left]
                max_price = max(max_price, finalPrice)
            else:
            # jump left to right
                left = right
            # move right forward
            right += 1
        return max_price
