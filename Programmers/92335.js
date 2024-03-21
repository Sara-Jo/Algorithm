function solution(n, k) {
  let convertedNum;

  if (k === 10) convertedNum = String(n);
  else {
    let temp = [];
    while (n >= k) {
      temp.push(n % k);
      n = Math.floor(n / k);
    }
    if (n !== 0) temp.push(n);
    temp.reverse();
    convertedNum = temp.join("");
  }

  let divided = convertedNum.split("0");
  let answer = 0;

  divided.forEach((d) => {
    if (d && isPrime(d)) answer += 1;
  });

  return answer;
}

function isPrime(n) {
  n = Number(n);
  if (n === 1) return false;
  if (n === 2) return true;

  for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    if (n % i === 0) return false;
  }
  return true;
}
