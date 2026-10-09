class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in f:
                l = max(f[s[r]] + 1, l)
            f[s[r]] = r
            res = max(res, r -l + 1)
        return res