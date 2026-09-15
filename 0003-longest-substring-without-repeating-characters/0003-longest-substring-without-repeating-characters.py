class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        C = set()
        L = 0
        RES = 0

        for r in range(len(s)):
            while s[r] in C:
                C.remove(s[L])
                L += 1
            C.add(s[r])
            RES = max(RES, r-L+1)
        return RES
        