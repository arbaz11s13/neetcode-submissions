class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_lin(nums[1:]), self.rob_lin(nums[:-1]))
        
    def rob_lin(self, nums):

        rob_last, rob_sl = 0, 0
        for num in nums:
            temp = max(num + rob_sl, rob_last)
            rob_sl = rob_last
            rob_last = temp
        return rob_last
    
    # return max(nums[0], rob(nums[1:]), rob(nums[:-1]))