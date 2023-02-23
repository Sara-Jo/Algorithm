class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]

        if numRows == 1:
            return answer

        for i in range(numRows - 1):
            temp = [1]
            for j in range(i): 
                temp.append(answer[i][j] + answer[i][j+1])
            temp.append(1)
            answer.append(temp)

        return answer