class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #-------------1-------------
        # total = []
        # for i in range(n):
        #     for j in range(n):
        #         total.append(matrix[i][j])
        # return sorted(total)[k - 1]

        #-------------2-------------
        n, start, end = len(matrix), matrix[0][0], matrix[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n - 1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: 
                    j -= 1
                cnt += (j + 1)
            return cnt
         
        while start < end:
            mid = (start + end) // 2
            if check(mid) < k:
                start = mid + 1
            else:
                end = mid
                
        return start