class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = int(str(abs(x))[::-1]) * sign

        if abs(x) > 2**31 - 1:
            return 0

        return x