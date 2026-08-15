class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        nums.sort(key=lambda x: -counter[x])
        # print(nums)
        ans = set()
        count = 0
        for num in nums:
            if count == k:
                break
            if num not in ans:
                ans.add(num)
                count += 1
        return list(ans)
            