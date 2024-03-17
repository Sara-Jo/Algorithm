function solution(id_list, report, k) {
  let reportCount = {};
  let reportHistory = [...Array(id_list.length)].map(() => []);

  report.forEach((r) => {
    const [a, b] = r.split(" ");
    const reporterIndex = id_list.findIndex((id) => id === a);

    if (!reportHistory[reporterIndex].includes(b)) {
      reportHistory[reporterIndex].push(b);

      if (reportCount[b]) reportCount[b] += 1;
      else reportCount[b] = 1;
    }
  });

  let bannedId = [];
  for (id in reportCount) {
    if (reportCount[id] >= k) bannedId.push(id);
  }

  let answer = [...Array(id_list.length)].fill(0);
  reportHistory.forEach((r, i) => {
    bannedId.forEach((b) => {
      if (r.includes(b)) answer[i] += 1;
    });
  });
  console.log(reportCount);
  return answer;
}
