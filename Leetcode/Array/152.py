class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product, min_product, answer = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_product * nums[i], min_product * nums[i])
            y = min(nums[i], max_product * nums[i], min_product * nums[i])
            max_product, min_product = x, y
            answer = max(max_product, answer)

        return answer