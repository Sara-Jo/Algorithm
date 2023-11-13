function solution(n, stations, w) {
  const W = w * 2 + 1;
  let start = 1;
  let answer = 0;

  stations.forEach((station) => {
    answer += Math.max(Math.ceil((station - w - start) / W), 0);
    start = station + w + 1;
  });

  if (start <= n) {
    answer += Math.ceil((n - start + 1) / W);
  }

  return answer;
}
