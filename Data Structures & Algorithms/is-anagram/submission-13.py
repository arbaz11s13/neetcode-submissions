class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs, ft = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            fs[s[i]] = 1 + fs.get(s[i], 0)
            ft[t[i]] = 1 + ft.get(t[i], 0)

        return fs == ft