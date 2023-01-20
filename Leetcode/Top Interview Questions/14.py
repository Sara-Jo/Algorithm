class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        firstWord = strs[0]
        i = 0
        while i < len(firstWord):
            for str in strs:
                if str[i] != firstWord[i]:
                    return "" if i == 0 else firstWord[:i]
            i += 1
        return firstWord