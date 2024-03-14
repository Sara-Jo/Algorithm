function solution(friends, gifts) {
  const n = friends.length;
  let giftHistory = [...Array(n)].map(() => [...Array(n)].fill(0)); //  주고받은 선물
  let giftIndex = [...Array(n)].map(() => [0, 0, 0]); // 선물 지수

  gifts.forEach((gift) => {
    const [sender, receiver] = gift.split(" ");
    const senderIndex = friends.findIndex((friend) => friend === sender);
    const receiverIndex = friends.findIndex((friend) => friend === receiver);
    giftHistory[senderIndex][receiverIndex] += 1;
    giftIndex[senderIndex][0] += 1;
    giftIndex[receiverIndex][1] += 1;
  });

  giftIndex.forEach((g) => {
    g[2] = g[0] - g[1];
  });

  let giftCount = [...Array(n)].fill(0);

  for (let i = 0; i < n - 1; i++) {
    for (let j = i + 1; j < n; j++) {
      // 두 사람이 선물 주고받은 기록이 있고, 주고받은 수가 다른 경우
      if (giftHistory[i][j] !== giftHistory[j][i]) {
        if (giftHistory[i][j] > giftHistory[j][i]) {
          giftCount[i] += 1;
        } else {
          giftCount[j] += 1;
        }
      } else if (giftIndex[i][2] !== giftIndex[j][2]) {
        if (giftIndex[i][2] > giftIndex[j][2]) {
          giftCount[i] += 1;
        } else {
          giftCount[j] += 1;
        }
      }
    }
  }

  return Math.max(...giftCount);
}
