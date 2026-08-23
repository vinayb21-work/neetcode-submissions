class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            curr = 1
            left, right = num - 1, num + 1
            while left in numSet:
                visited.add(left)
                curr += 1
                left -= 1
            while right in numSet:
                visited.add(right)
                curr += 1
                right += 1
            ans = max(ans, curr)
        return ans