class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i, c in enumerate(s):
            if not c in s[i+1:]:
                continue
            else:
                for j in range(i + 1, len(s)):
                    tmp = s[i:j+1]
                    if s[j] == c and tmp == tmp[::-1] and len(tmp) > len(result):
                        result = tmp

        return result if len(result) > 0 else s[0]