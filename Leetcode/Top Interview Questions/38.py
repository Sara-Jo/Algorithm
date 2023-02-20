class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            temp = ""
            while s:
                count = 1
                for i in range(1, len(s)):
                    if s[i] == s[0]:
                        count += 1
                    else:
                        break
                temp += str(count)
                temp += s[0]
                s = s[count:]
            s = temp
        return s
