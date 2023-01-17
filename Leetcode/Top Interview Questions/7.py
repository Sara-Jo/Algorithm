class Solution:
    def reverse(self, x: int) -> int:
        # 1---------------------------------------
        # sign = 1 
        # if x < 0:
        #     sign = -1
        #     x = -x

        # arr = []
        # while x > 0:
        #     arr.append(x % 10)
        #     x //= 10

        # answer = 0
        # for n in arr:
        #     answer = answer * 10 + n

        # answer *= sign

        # return answer if -2147483648 <= answer <= 2147483647 else 0


        # 2---------------------------------------
        if x < 0:
            sign = -1
        else:
            sign = 1

        answer = sign * int(str(abs(x))[::-1])
        
        return answer if -(2**31) <= answer <= 2**31 - 1 else 0