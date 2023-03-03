class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for _ in range(n):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1