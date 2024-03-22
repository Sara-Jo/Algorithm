function solution(s) {
  let tuples = [];

  s = s.slice(2, s.length - 2).split("},{");
  s.forEach((nums) => {
    tuples.push(nums.replace("[{}]g", "").split(",").map(Number));
  });
  tuples.sort((a, b) => a.length - b.length);

  let answer = [];
  for (let i = 0; i < tuples.length; i++) {
    if (i === 0) answer = [...tuples[0]];
    else {
      tuples[i].forEach((num) => {
        if (answer.indexOf(num) === -1) answer.push(num);
      });
    }
  }

  return answer;
}
