class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            smaller = nums2
            bigger = nums1
        else:
            bigger = nums2
            smaller = nums1

        answer = []
        for num in smaller:
            if num in bigger:
                answer.append(num)
                bigger.remove(num)

        return answer