function solution(queue1, queue2) {
  let sum1 = queue1.reduce((a, b) => a + b, 0);
  let sum2 = queue2.reduce((a, b) => a + b, 0);
  const half = (sum1 + sum2) / 2;
  const q = [...queue1, ...queue2];
  const n = queue1.length;
  let pointer1 = 0;
  let pointer2 = n;

  for (let count = 0; count < n * 3; count++) {
    if (sum1 === half) return count;
    else if (sum1 > half) {
      sum1 -= q[pointer1];
      pointer1++;
    } else {
      sum1 += q[pointer2];
      pointer2++;
    }
  }

  return -1;
}
