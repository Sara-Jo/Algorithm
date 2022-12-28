class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': 1, ')': 1, '{': 2, '}': 2, '[': 3, ']': 3}
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) > 0:
                last = stack.pop()
                if dict[last] != dict[s[i]]:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False