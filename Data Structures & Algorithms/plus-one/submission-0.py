class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        ans = []
        for digit in digits:
            stack.append(digit)
        stack[-1] = stack[-1]
        carry = 1
        while stack:
            top = stack.pop() + carry
            if top < 10:
                ans.append(top)
                carry = 0
            else:
                ans.append(top % 10)
                carry = 1
        if carry:
            ans.append(1)
        return ans[::-1]
                
