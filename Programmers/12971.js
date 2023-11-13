function solution(sticker) {
  let len = sticker.length;
  if (len === 1) return sticker[0];

  let dp1 = Array(len).fill(0);
  let dp2 = Array(len).fill(0);

  dp1[0] = sticker[0];
  dp1[1] = sticker[0];

  dp2[1] = sticker[1];

  for (let i = 2; i < len - 1; i++) {
    dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
  }

  for (let i = 2; i < len; i++) {
    dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
  }

  val1 = Math.max.apply(null, dp1);
  val2 = Math.max.apply(null, dp2);

  return Math.max(val1, val2);
}
