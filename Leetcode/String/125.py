class Solution:
    def isPalindrome(self, s: str) -> bool:
        #----------------1--------------------
        # stack = []
        # for x in s:
        #     if x.isalpha():
        #         stack.append(x.lower())
        #     elif x.isdigit():
        #         stack.append(x)
        # return True if stack == list(reversed(stack)) else False

        #----------------2--------------------
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True