/*  
items: 선택한 요소를 담는 배열
k: list 중에서 선택하는 개수 
**/
function permutation(items, list, k, result) {
  if (items.length === k) {
    result.push(items);
    return;
  }

  for (let i = 0; i < list.length; i++) {
    permutation(
      [...items, list[i]],
      list.filter((v, j) => j !== i),
      k,
      result
    );
  }
}

function permutationWithRepetition(items, list, k, result) {
  if (items.length === k) {
    result.push(items);
    return;
  }

  for (let i = 0; i < list.length; i++) {
    permutationWithRepetition([...items, list[i]], list, k, result);
  }
}

const list = [1, 2, 3, 4];

let result1 = [];
permutation([], list, 2, result1);
console.log(result1);

let result2 = [];
permutationWithRepetition([], list, 2, result2);
console.log(result2);
