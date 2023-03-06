class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)
        for num in nums:
            if arr[num] >= 1:
                return num
            else:
                arr[num] += 1