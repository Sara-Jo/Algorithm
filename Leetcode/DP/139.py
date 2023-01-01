class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #-------------1---------------
    #     word_set = set(wordDict)
    #     q = deque()
    #     visited = set()

    #     q.append(0)
    #     while q:
    #         start = q.popleft()
    #         if start in visited:
    #             continue
    #         for end in range(start + 1, len(s) + 1):
    #             if s[start:end] in word_set:
    #                 q.append(end)
    #                 if end == len(s):
    #                     return True
    #         visited.add(start)
    #     return False

    #-------------2---------------
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]