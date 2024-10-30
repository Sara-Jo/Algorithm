/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function (dictionary, sentence) {
  dictionary.sort((a, b) => a.length - b.length);
  const sentenceArr = sentence.split(" ");

  let answerArr = [];
  for (const word of sentenceArr) {
    for (let i = 0; i < dictionary.length; i++) {
      // 현재 단어가 derivative이면, answer에 추가하고 반복문 break
      if (
        word.length >= dictionary[i].length &&
        word.slice(0, dictionary[i].length) === dictionary[i]
      ) {
        answerArr.push(dictionary[i]);
        break;
      }
      // derivative가 아니면, 단어 그대로 answer에 추가
      if (i === dictionary.length - 1) {
        answerArr.push(word);
      }
    }
  }

  return answerArr.join(" ");
};
