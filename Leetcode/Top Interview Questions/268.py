class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #----------1-----------
        # for x in range(len(nums) + 1):
        #     if x not in nums:
        #         return x

        #----------2-----------
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)