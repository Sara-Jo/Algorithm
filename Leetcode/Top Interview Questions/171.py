class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        for c in columnTitle:
            answer = answer * 26 +(ord(c) - 64)
        return answer