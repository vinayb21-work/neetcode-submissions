class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        posMap = defaultdict(list)
        for index, num in enumerate(nums):
            rem = target - num
            if rem in posMap:
                return [posMap[rem][0], index]
            posMap[num].append(index)
        