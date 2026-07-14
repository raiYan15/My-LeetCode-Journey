class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for ch in s.lower():
            if ch.isalnum():
                c += ch
        l, r = 0, len(c) - 1
        while l < r:
            if c[l] != c[r]:
                return False
            l += 1
            r -= 1
        return True