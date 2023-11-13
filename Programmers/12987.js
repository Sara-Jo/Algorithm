function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);

  const len = A.length;
  let answer = 0;
  let j = 0;

  for (let i = 0; i < len; i++) {
    while (A[i] >= B[j] && j < len) j += 1;
    if (j === len) break;
    else {
      answer += 1;
      j += 1;
    }
  }

  return answer;
}
