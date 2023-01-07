class Solution:
    def countSubstrings(self, s: str) -> int:
        result = len(s)
        for i, c in enumerate(s):
            if c in s[i+1:]:
                for j in range(i + 1, len(s)):
                    tmp = s[i:j+1]
                    if c == s[j] and tmp == tmp[::-1]:
                        result += 1

        return result