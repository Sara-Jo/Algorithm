class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        #-------------1----------------
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return i
        # return len(nums) - 1   

        #-------------2----------------
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

