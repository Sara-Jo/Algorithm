function solution(cap, n, deliveries, pickups) {
  let del_sum = deliveries.reduce((a, b) => a + b, 0);
  let pick_sum = pickups.reduce((a, b) => a + b, 0);

  let answer = 0;

  while (del_sum > 0 || pick_sum > 0) {
    // 끝에서부터 0인 원소 지우기
    deleteZeros(deliveries);
    deleteZeros(pickups);

    // 끝에서 부터 왕복 거리 다녀오기
    let len = Math.max(deliveries.length, pickups.length);
    answer += len * 2;

    // 배달 및 수거
    del_sum -= deliverOrPickup(cap, deliveries);
    pick_sum -= deliverOrPickup(cap, pickups);
  }

  return answer;
}

function deleteZeros(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] === 0) arr.pop();
    else return;
  }
}

function deliverOrPickup(cap, arr) {
  let sum = 0;

  for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] >= cap) {
      arr[i] -= cap;
      sum += cap;
      break;
    } else {
      cap -= arr[i];
      sum += arr[i];
      arr[i] = 0;
    }
  }
  return sum;
}
