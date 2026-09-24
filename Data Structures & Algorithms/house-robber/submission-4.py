class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_last, rob_sl = 0, 0

        for num in nums:
            temp = max( num + rob_sl, rob_last)
            rob_sl = rob_last
            rob_last = temp
        return rob_last
