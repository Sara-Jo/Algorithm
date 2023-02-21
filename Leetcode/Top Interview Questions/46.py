class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(arr):
            if len(arr) == len(nums):
                answer.append(arr[:])
                return
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    dfs(arr)
                    arr.pop()

        dfs([])
        return answer 
        