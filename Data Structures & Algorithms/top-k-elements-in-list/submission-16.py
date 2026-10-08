class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i, n in enumerate(nums):
            freq[n] = 1 + freq.get(n, 0)

        sorted_dict = dict(sorted(freq.items(), key = lambda item: item[1], reverse= True))
        res = list(sorted_dict.keys())
        return res[:k]