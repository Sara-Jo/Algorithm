class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        i = 0
        sign = 1

        if len(s) == 0:
            return 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < len(s) and '0' <= s[i] <= '9':
            answer = answer * 10 + int(s[i])
            i += 1

        answer = answer * sign

        if answer < -(2**31):
            return -(2**31)
        elif answer > (2**31) - 1:
            return (2**31) - 1
        else:
            return answer
            