class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[0]

        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        with_first_house = dp[len(nums) - 2]

        dp = [0] * len(nums)
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        without_first_house = dp[len(nums) - 1]

        return max(with_first_house, without_first_house)