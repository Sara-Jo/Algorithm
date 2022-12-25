class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #-------------1---------------
        # if target not in nums:
        #     return -1
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i

        #-------------2---------------
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1