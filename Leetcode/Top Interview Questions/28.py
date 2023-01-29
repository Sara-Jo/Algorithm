class Solution:
    def check(self, haystack: str, needle: str) -> bool:
        if len(haystack) < len(needle):
            return False

        for i in range(len(needle)):
            if haystack[i] != needle[i]:
                return False
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        start = needle[0]
        for i, c in enumerate(haystack):
            if c == start:
                if self.check(haystack[i:], needle):
                    return i
        return -1