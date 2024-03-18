function solution(users, emoticons) {
  const percentage = [10, 20, 30, 40];

  // 조합 구하기
  let cases = [[]];
  for (let i = 0; i < emoticons.length; i++) {
    let temp = [];
    cases.forEach((c) => {
      percentage.forEach((p) => {
        temp.push([...c, p]);
      });
    });
    cases = temp;
  }

  let answer = [0, 0];
  cases.forEach((c) => {
    let plus = 0;
    let sumAmount = 0;
    users.forEach(([per, price]) => {
      let sumPrice = 0;
      emoticons.forEach((emo, i) => {
        if (c[i] >= per) sumPrice += (emo / 100) * (100 - c[i]); // 할인가로 이모티콘 구매했을때 총 가격
      });
      if (sumPrice >= price) plus += 1; // 플러스 가입
      else sumAmount += sumPrice; // 이모티콘 구매
    });

    if (answer[0] < plus || (answer[0] === plus && answer[1] < sumAmount))
      answer = [plus, sumAmount];
  });

  return answer;
}
