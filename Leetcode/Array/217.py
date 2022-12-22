class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # ------------1-------------
        # seen = {}
        # for num in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen[num] = 1
        # return False

        # ------------2-------------
        # return len(nums) != len(set(nums))

        # ------------3-------------
        nset = set()
        for num in nums:
            if num in nset:
                return True
            else:
                nset.add(num)