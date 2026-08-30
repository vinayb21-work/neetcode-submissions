class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMin, currMax = 1, 1
        for num in nums:
            temp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(currMin * num, temp, num)
            ans = max(ans, currMax)
        return ans