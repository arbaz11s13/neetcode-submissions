class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs, ft = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            c1 = s[i].lower()
            c2 = t[i].lower()
            fs[c1] = 1 + fs.get(c1, 0)
            ft[c2] = 1 + ft.get(c2, 0)
        
        return fs == ft