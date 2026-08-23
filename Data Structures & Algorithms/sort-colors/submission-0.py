class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        n = len(nums)
        i = 0
        vals = [0, 1, 2]
        for j in vals:
            for _ in range(counter[j]):
                nums[i] = j
                i += 1
        return nums