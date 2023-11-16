function solution(gems) {
  const setCount = new Set(gems).size;
  const gemMap = new Map();
  let gemLengths = [];

  gems.forEach((gem, i) => {
    gemMap.delete(gem);
    gemMap.set(gem, i);

    if (gemMap.size === setCount) {
      gemLengths.push([gemMap.values().next().value + 1, i + 1]);
    }
  });

  gemLengths.sort((a, b) => {
    if (a[1] - a[0] === b[1] - b[0]) {
      return a[0] - b[0];
    }
    return a[1] - a[0] - (b[1] - b[0]);
  });

  return gemLengths[0];
}
