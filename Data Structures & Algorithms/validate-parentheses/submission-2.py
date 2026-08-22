class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspondingChar = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                corresponder = correspondingChar[char]
                if stack and stack[-1] == corresponder:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0