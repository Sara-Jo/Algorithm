/*  
items: 선택한 요소를 담는 배열
idx: list의 인덱스
k: list 중에서 선택하는 개수 
**/
function combination(items, idx, list, k, result) {
  if (items.length === k) {
    result.push(items);
    return;
  }

  for (let i = idx; i < list.length; i++) {
    combination([...items, list[i]], i + 1, list, k, result);
  }
}

function combinationWithRepetition(items, idx, list, k, result) {
  if (items.length === k) {
    result.push(items);
    return;
  }

  for (let i = idx; i < list.length; i++) {
    combinationWithRepetition([...items, list[i]], i, list, k, result);
  }
}

const list = [1, 2, 3, 4];

let result1 = [];
combination([], 0, list, 2, result1);
console.log(result1);

let result2 = [];
combinationWithRepetition([], 0, list, 2, result2);
console.log(result2);
