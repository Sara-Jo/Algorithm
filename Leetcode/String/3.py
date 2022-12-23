class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            seen = []
            for j in range(i, len(s)):
                if s[j] in seen:
                    answer = max(answer, j - i)
                    break
                else:
                    seen.append(s[j])
                    answer = max(answer, len(seen))
        
        return answer