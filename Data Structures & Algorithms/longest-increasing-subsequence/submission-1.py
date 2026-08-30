from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        dp.append(nums[0])
        ans = 1
        for i in range(1, n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                ans += 1
                continue
            index = bisect_left(dp, nums[i])
            dp[index] = nums[i]
        return ans
