/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function (words, k) {
  let wordMap = new Map();
  words.sort();

  for (const word of words) {
    if (wordMap.has(word)) {
      const count = wordMap.get(word);
      wordMap.set(word, count + 1);
    } else {
      wordMap.set(word, 1);
    }
  }

  let wordArr = [...wordMap];
  wordArr.sort((a, b) => b[1] - a[1]);

  let answer = [];
  for (let i = 0; i < k; i++) {
    answer.push(wordArr[i][0]);
  }

  return answer;
};
