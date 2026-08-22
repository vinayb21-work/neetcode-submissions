class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                ans[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return ans