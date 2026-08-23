class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        
        def generate(i, subset):
            if i == n:
                self.ans.append(subset[::])
                return
            
            subset.append(nums[i])
            generate(i+1, subset)
            subset.pop()
            generate(i+1, subset)
        
        generate(0, [])

        return self.ans
