import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(k):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile / k)
            return ans
        
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hours = hoursTaken(mid)
            if hours <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans