class Solution:
    def romanToInt(self, s: str) -> int:
        #------------------1----------------------
        # answer = 0
        # symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        # values = [1, 5, 10, 50, 100, 500, 1000]

        # for i, c in enumerate(s):
        #     if i > 0:
        #         if s[i - 1] == 'I':
        #             if c == 'V':
        #                 answer -= 1
        #                 answer += 4
        #                 continue
        #             if c == 'X':
        #                 answer -= 1
        #                 answer += 9
        #                 continue
        #         if s[i - 1] == 'X':
        #             if c == 'L':
        #                 answer -= 10
        #                 answer += 40
        #                 continue
        #             if c == 'C':
        #                 answer -= 10
        #                 answer += 90
        #                 continue
        #         if s[i - 1] == 'C':
        #             if c == 'D':
        #                 answer -= 100
        #                 answer += 400
        #                 continue
        #             if c == 'M':
        #                 answer -= 100
        #                 answer += 900
        #                 continue

        #     i = symbols.index(c)
        #     answer += values[i]

        # return answer

        #------------------2----------------------
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        answer = 0
        for c in s:
            answer += symbols[c]
        
        return answer