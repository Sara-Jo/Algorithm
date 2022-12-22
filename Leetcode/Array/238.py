class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = []
        tmp = 1
        for num in nums:
            answer.append(tmp)
            tmp *= num

        tmp = 1
        for i in reversed(range(len(nums))):
            answer[i] *= tmp
            tmp *= nums[i]

        return answer