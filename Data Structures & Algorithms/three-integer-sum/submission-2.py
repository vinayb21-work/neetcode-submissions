class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rem = -nums[i]
            left, right = i+1, n-1
            while left < right:
                while left < right and left - 1 > i and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if left == right:
                    break
                currSum = nums[left] + nums[right]
                if currSum == rem:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif currSum > rem:
                    right -= 1
                else:
                    left += 1
        return ans