class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #---------------1------------------
        # is_started = False
        # answer = []
        # for i in range(len(nums)):
        #     if not is_started and nums[i] == target:
        #         answer.append(i)
        #         is_started = True
        #     if (nums[i] == target and i == len(nums) - 1) or (nums[i] == target and nums[i + 1] != target):
        #         answer.append(i)
        # if len(answer) == 0:
        #     return [-1, -1]
        # else:
        #     return answer

        #---------------2------------------
        def searchLeft(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def searchRight(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left = searchLeft(nums, target)
        right = searchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
            
        #---------------3------------------
        # def search(target):
        #     left = 0
        #     right = len(nums) - 1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if nums[mid] >= target:
        #             right = mid
        #         else:
        #             left = mid + 1
        #     return left
        
        # left = search(target)
        # return [left, search(target + 1) - 1] if target in nums[left:left+1] else [-1, -1]