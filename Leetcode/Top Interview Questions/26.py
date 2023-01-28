class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if nums[prev] != num:
                nums[prev + 1] = num
                prev += 1

        return prev + 1