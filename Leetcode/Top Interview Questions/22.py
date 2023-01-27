class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #-----------------1--------------------
        # def generate(a = []):
        #     if len(a) == 2 * n:
        #         if valid(a):
        #             answer.append("".join(a))
        #     else:
        #         a.append('(')
        #         generate(a)
        #         a.pop()
        #         a.append(')')
        #         generate(a)
        #         a.pop()

        # def valid(a):
        #     bal = 0
        #     for c in a:
        #         if c == '(':
        #             bal += 1
        #         else:
        #             bal -= 1
        #         if bal < 0:
        #             return False
        #     return bal == 0
        
        # answer = []
        # generate()
        # return answer

        #-----------------2--------------------
        answer = []
        def backtrack(s = [], left = 0, right = 0):
            if len(s) == 2 * n:
                answer.append("".join(s))
                return
            if left < n:
                s.append("(")
                backtrack(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(s, left, right + 1)
                s.pop()
        
        backtrack()
        return answer