class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        temp = x
        rev = 0

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        return temp == rev