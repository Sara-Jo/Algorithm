from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #------------1-------------
        # answer = [[]]
        # for i in range(1, len(nums) + 1):
        #     temp = list(combinations(nums, i))
        #     for x in temp:
        #         answer.append(x)
        # return answer

        #------------2-------------
        # answer = [[]]
        # for num in nums:
        #     answer += [curr + [num] for curr in answer]
        # return answer

        #------------3-------------
        def backtracking(curr, n, start):
            if len(curr) == n:
                answer.append(curr[:])
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtracking(curr, n, start + 1)
                curr.pop()
        
        answer = [[]]
        for i in range(1, len(nums) + 1):
            backtracking([], i, 0)

        return answer