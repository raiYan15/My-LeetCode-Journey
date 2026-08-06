class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            p = 1
            x = n

            while x > 0:
                p *= x % 10
                x //= 10

            if p % t == 0:
                return n

            n += 1