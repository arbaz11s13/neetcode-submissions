class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}

        for i,C in enumerate(s):
            c = C.lower()
            freq_s[c] = 1 + freq_s.get(c, 0)

        for i,C in enumerate(t):
            c = C.lower()
            freq_t[c] = 1 + freq_t.get(c, 0)

        return freq_s == freq_t