class Solution:
    def reverse(self, x: int) -> int:
        lower, upper = -2**31, 2**31 - 1
        reverse = 0
        negative = x < 0
        x = abs(x)
        while x > 0:
            reverse *= 10
            reverse += x % 10
            x //= 10
        if negative:
            reverse *= -1
        # print(reverse)
        return reverse if lower <= reverse <= upper else 0
        