class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs, ft = {}, {}

        for i, c in enumerate(s):
            fs[c] = 1 + fs.get(c, 0)

        for i, c in enumerate(t):
            ft[c] = 1 + ft.get(c, 0)
        
        return fs == ft