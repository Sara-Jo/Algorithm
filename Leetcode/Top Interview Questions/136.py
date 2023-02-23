class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #---------1---------
        # for i in range(len(nums)):
        #     if nums[i] in nums[:i]:
        #         continue
        #     if nums[i] in nums[i + 1:]:
        #         continue
        #     return nums[i]

        #---------2---------
        xor = 0
        for num in nums:
            xor ^= num
        return xor