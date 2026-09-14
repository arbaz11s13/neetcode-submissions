class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i,n in enumerate(nums):
            comp = target - n

            for j in range(i,len(nums)):
                if nums[j] == comp and i !=j:
                    res.append(i)
                    res.append(j)
        
        return res

