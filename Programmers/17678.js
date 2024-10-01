function solution(n, t, m, timetable) {
  // 분 단위로 시간 변환
  timetable = timetable.map((time) => {
    const [h, m] = time.split(":");
    return h * 60 + Number(m);
  });

  // 오름차순 정렬
  timetable.sort((a, b) => a - b);

  let time = 9 * 60;
  for (let i = 0; i < n; i++) {
    // 현재 셔틀보다 빨리 온 사람 수 (탈수있는 사람 수)
    const canGoCount = timetable.filter((a) => a <= time).length;

    // 셔틀이 막차고, 셔틀이 꽉 찬 경우 마지막 크루보다 1분 먼저 도착
    if (i === n - 1) {
      if (canGoCount >= m) time = timetable[m - 1] - 1;
    } else {
      // 막차 아닌 경우, 탈 수 있는 인원을 자르고 time 업데이트
      timetable.splice(0, canGoCount > m ? m : canGoCount);
      time += t;
    }
  }

  return (
    String(Math.floor(time / 60)).padStart(2, "0") +
    ":" +
    String(time % 60).padStart(2, "0")
  );
}
