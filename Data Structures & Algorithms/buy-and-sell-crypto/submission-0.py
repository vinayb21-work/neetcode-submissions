class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        stack = []
        minPrice = float("inf")
        for price in prices:
            while stack and stack[-1][0] >= price:
                stack.pop()
            minPrice = min(minPrice, price)
            stack.append((price, minPrice))
            ans = max(ans, price - minPrice)
        return ans