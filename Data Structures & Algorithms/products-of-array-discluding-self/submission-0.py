class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        leftProduct = [num for num in nums]
        rightProduct = [num for num in nums]
        n = len(nums)
        for i in range(1, n):
            leftProduct[i] = leftProduct[i-1] * nums[i]
            rightProduct[n-i-1] = rightProduct[n-i] * nums[n-i-1]
        ans = [0 for _ in range(n)]
        ans[0] = rightProduct[1]
        ans[-1] = leftProduct[-2]
        for i in range(1, n-1):
            ans[i] = leftProduct[i-1] * rightProduct[i+1]
        return ans
