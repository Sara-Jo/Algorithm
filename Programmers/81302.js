function solution(places) {
  let answer = [];
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];

  places.forEach((place) => {
    place.forEach((row, i) => (place[i] = row.split("")));
    let shouldBreak = false;
    for (let x = 0; x < 5; x++) {
      for (let y = 0; y < 5; y++) {
        let count = 0;
        for (let i = 0; i < 4; i++) {
          let nx = x + dx[i];
          let ny = y + dy[i];
          if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
            if (place[x][y] == "P" && place[nx][ny] == "P") {
              answer.push(0);
              shouldBreak = true;
              break;
            } else if (place[x][y] == "O" && place[nx][ny] == "P") {
              count += 1;
              if (count >= 2) {
                answer.push(0);
                shouldBreak = true;
                break;
              }
            }
          }
        }
        if (shouldBreak) break;
      }
      if (shouldBreak) break;
    }
    if (!shouldBreak) answer.push(1);
  });

  return answer;
}
