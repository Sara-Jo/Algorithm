# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1) == True:
            return 1
        start = 2
        end = n ** 31 - 1
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid) == True and isBadVersion(mid - 1) == False:
                return mid
            elif isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
