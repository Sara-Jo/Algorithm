function solution(fees, records) {
  let inouts = {};
  let timeSum = {};

  records.forEach((record) => {
    let [time, car, type] = record.split(" ");
    let [h, m] = time.split(":").map(Number);

    if (type === "IN") inouts[car] = h * 60 + m;
    else {
      if (timeSum[car]) timeSum[car] += h * 60 + m - inouts[car];
      else timeSum[car] = h * 60 + m - inouts[car];
      delete inouts[car];
    }
  });

  for (let car in inouts) {
    const out = 23 * 60 + 59;
    if (timeSum[car]) timeSum[car] += out - inouts[car];
    else timeSum[car] = out - inouts[car];
  }

  let prices = [];
  for (let car in timeSum) {
    if (timeSum[car] <= fees[0]) prices.push([car, fees[1]]);
    else
      prices.push([
        car,
        fees[1] + Math.ceil((timeSum[car] - fees[0]) / fees[2]) * fees[3],
      ]);
  }

  prices.sort((a, b) => a[0] - b[0]);
  return prices.map((p) => p[1]);
}
