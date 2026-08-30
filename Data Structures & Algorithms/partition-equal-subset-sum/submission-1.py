from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        @cache
        def check(i, sum1, sum2):
            if i == n:
                return sum1 == sum2
            
            return (
                check(i+1, sum1 + nums[i], sum2) or
                check(i+1, sum1, sum2 + nums[i])
            )
        
        return check(0, 0, 0)