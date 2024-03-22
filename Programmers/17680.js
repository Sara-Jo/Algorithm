function solution(cacheSize, cities) {
  if (cacheSize === 0) return cities.length * 5;

  let answer = 0;
  let cache = [];

  cities.forEach((city) => {
    let i = cache.indexOf(city.toLowerCase());
    if (i === -1) {
      if (cache.length === cacheSize) cache.shift();
      answer += 5;
    } else {
      answer += 1;
      cache.splice(i, 1);
    }
    cache.push(city.toLowerCase());
  });

  return answer;
}
