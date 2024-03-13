function solution(line) {
  const n = line.length;
  const crossPoints = [];
  let minX = Infinity;
  let maxX = -Infinity;
  let minY = Infinity;
  let maxY = -Infinity;

  // 정수 교점 찾기
  for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      const [a, b, e] = line[i];
      const [c, d, f] = line[j];
      const mod = a * d - b * c;

      if (!mod) continue; // 두 직선이 평행 또는 일치하는 경우

      const xNumerator = b * f - e * d;
      const yNumerator = e * c - a * f;

      if (xNumerator % mod || yNumerator % mod) continue; // 정수 좌표가 아닌 경우

      const xPoint = xNumerator / mod;
      const yPoint = yNumerator / mod;
      crossPoints.push([xPoint, yPoint]);

      // 최대, 최소값 갱신
      minX = Math.min(minX, xPoint);
      maxX = Math.max(maxX, xPoint);
      minY = Math.min(minY, yPoint);
      maxY = Math.max(maxY, yPoint);
    }
  }

  let answer = [...Array(maxY - minY + 1)].map(() =>
    [...Array(maxX - minX + 1)].map(() => ".")
  );

  // 교점을 1사분면으로 옮겨주기 (중심점 이동), y축은 거꾸로 그려주기
  crossPoints.forEach(([x, y]) => {
    answer[maxY - y][x - minX] = "*";
  });

  return answer.map((v) => v.join(""));
}
