/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  const vals = [];
  let curr = head;

  while (curr) {
    vals.push(curr.val);
    curr = curr.next;
  }

  curr = head;

  for (let i = 0, j = vals.length - 1; i < vals.length && j >= 0; i++, j--) {
    if (i <= j) {
      curr.val = vals[i];
      curr = curr.next;
    }
    if (!curr) return;
    else if (i !== j) {
      curr.val = vals[j];
      curr = curr.next;
    }
  }
};
