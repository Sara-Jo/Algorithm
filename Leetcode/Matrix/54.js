/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  let up = 0;
  let down = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;
  let direction = 0; // 0: right, 1: down, 2: left, 3: up
  let answer = [];

  function goRight() {
    for (let i = left; i <= right; i++) answer.push(matrix[up][i]);
    up++;
  }

  function goDown() {
    for (let i = up; i <= down; i++) answer.push(matrix[i][right]);
    right--;
  }

  function goLeft() {
    for (let i = right; i >= left; i--) answer.push(matrix[down][i]);
    down--;
  }

  function goUp() {
    for (let i = down; i >= up; i--) answer.push(matrix[i][left]);
    left++;
  }

  while (left <= right && up <= down) {
    if (direction === 0) goRight();
    else if (direction === 1) goDown();
    else if (direction === 2) goLeft();
    else if (direction === 3) goUp();
    direction = (direction + 1) % 4;
  }

  return answer;
};
