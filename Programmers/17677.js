function solution(str1, str2) {
  let arr1 = [];
  let arr2 = [];

  for (let i = 0; i < str1.length - 1; i++) {
    if (isAlpha(str1[i]) && isAlpha(str1[i + 1]))
      arr1.push(str1.slice(i, i + 2).toUpperCase());
  }
  for (let i = 0; i < str2.length - 1; i++) {
    if (isAlpha(str2[i]) && isAlpha(str2[i + 1]))
      arr2.push(str2.slice(i, i + 2).toUpperCase());
  }

  const len1 = arr1.length;
  const len2 = arr2.length;
  if (len1 === 0 && len2 === 0) return 65536;

  let common_count = 0;
  arr1.forEach((pair) => {
    const idx = arr2.indexOf(pair);
    if (idx >= 0) {
      common_count += 1;
      arr2.splice(idx, 1);
    }
  });

  return Math.floor((common_count / (len1 + len2 - common_count)) * 65536);
}

function isAlpha(c) {
  if ((c >= "A" && c <= "Z") || (c >= "a" && c <= "z")) return true;
  else return false;
}
