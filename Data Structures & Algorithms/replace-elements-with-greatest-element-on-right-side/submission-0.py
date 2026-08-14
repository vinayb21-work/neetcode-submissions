class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        n = len(arr)
        ans = [-1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            while stack and stack[-1] < arr[i+1]:
                stack.pop()
            if not stack:
                stack.append(arr[i+1])
            ans[i] = stack[-1]
        return ans
