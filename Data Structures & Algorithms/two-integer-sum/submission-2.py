class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i,n in enumerate(nums):
            num_to_index[n] = i

        for i,n in enumerate(nums):
            complement = target - n

            if complement in num_to_index and num_to_index[complement] != i:
                return ([i,num_to_index[complement] ])
        return []
        