class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for n in nums:
            if n in frequency:
                frequency[n] +=1
            else:
                frequency[n] = 1
    
        sorted_dict = dict( sorted(frequency.items(), key = lambda item: item[1],reverse = True))
        res = list(sorted_dict.keys())
        return res[:k]
        