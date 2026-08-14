class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(filter(lambda x: 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57, s))
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True