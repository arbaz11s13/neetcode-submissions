class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq_s, freq_t = {}, {}

        for i in range(len(s)):
            freq_s[s[i].lower()] = 1 + freq_s.get(s[i].lower(), 0)
            freq_t[t[i].lower()] = 1 + freq_t.get(t[i].lower(), 0)

        # for i,C in enumerate(t):
        #     c = C.lower()
        #     freq_t[c] = 1 + freq_t.get(c, 0)

        return freq_s == freq_t