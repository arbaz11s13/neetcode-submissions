class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        shash = {}
        for i in s.lower():
            if i in shash:
                shash[i] += 1
            else:
                shash[i] = 1
        
        thash = {}
        for i in t.lower():
            if i in thash:
                thash[i] += 1
            else:
                thash[i] = 1
        
        if shash == thash:
            return True
        return False

