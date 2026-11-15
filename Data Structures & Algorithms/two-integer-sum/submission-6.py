class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, n in enumerate(nums):

            comp = target - n

            if comp in indices and indices[comp] != i:
                return [i, indices[comp]]
        
        return []