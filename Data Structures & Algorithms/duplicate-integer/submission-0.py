class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hmap = {}

        for i,n in enumerate(nums):
            hmap[n] = i

        for i,n in enumerate(nums):
            if n in hmap and hmap[n] !=i:
                return True
        return False
        