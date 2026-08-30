from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        @cache
        def check(i, target):
            if target == 0:
                return True
            
            if i >= n or target < 0:
                return False

            return (
                check(i+1, target - nums[i]) or
                check(i+1, target)
            )
        
        return check(0, target)