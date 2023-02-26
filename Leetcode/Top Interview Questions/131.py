class Solution:
    def partition(self, s: str) -> List[List[str]]: 
        result = []

        def dfs(curr, start):
            if start == len(s):
                result.append(curr[:])
                return
            for i in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:i]):
                    curr.append(s[start:i])
                    dfs(curr, i)
                    curr.pop()

        def isPalindrome(s):
            return s == s[::-1]

        dfs([], 0)
        return result