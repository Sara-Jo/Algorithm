function solution(stones, k) {
  let start = 1;
  let end = 200000000;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let count = 0;

    for (stone of stones) {
      if (stone <= mid) count++;
      else count = 0;
      if (count >= k) break;
    }

    if (count >= k) end = mid - 1;
    else start = mid + 1;
  }

  return start;
}
