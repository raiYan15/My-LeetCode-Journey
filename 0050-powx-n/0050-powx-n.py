class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative power
        if n < 0:
            return 1 / self.myPow(x, -n)
        # Base case
        if n == 0:
            return 1
        # If n is even
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        # If n is odd
        return x * self.myPow(x, n - 1)