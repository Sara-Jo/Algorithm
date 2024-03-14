function solution(today, terms, privacies) {
  let [today_y, today_m, today_d] = today.split(".").map(Number);
  let termsMap = {};

  terms.forEach((term) => {
    let [key, val] = term.split(" ");
    termsMap[key] = Number(val);
  });

  let answer = [];

  privacies.forEach((privacy, i) => {
    let [date, type] = privacy.split(" ");
    let [y, m, d] = date.split(".").map(Number);
    m += termsMap[type];

    let today_timestamp = today_y * 12 * 28 + today_m * 28 + today_d;
    let expire_timestamp = y * 12 * 28 + m * 28 + d;
    if (today_timestamp >= expire_timestamp) answer.push(i + 1);
  });

  return answer;
}
