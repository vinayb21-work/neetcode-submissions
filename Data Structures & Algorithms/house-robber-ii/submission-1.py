class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        def find(arr):
            n = len(arr)
            dp = [0 for _ in range(n+1)]
            dp[0] = 0
            dp[1] = arr[0]
            for i in range(2,n+1):
                dp[i] = max(dp[i-2] + arr[i-1], dp[i-1])
            return dp[-1]
        
        return max(
            find(nums[:-1]),
            find(nums[1:])
        )