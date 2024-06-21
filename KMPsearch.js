function matchTable(word) {
  const table = Array.from({ length: word.length }).fill(0);
  let prefixEnd = 0;
  let suffixEnd = 1;

  while (suffixEnd < word.length) {
    if (word[prefixEnd] === word[suffixEnd]) {
      // we can build a longer prefix based on this suffix
      // store the length of this longest prefix
      // move prefixEnd and suffixEnd
      prefixEnd++;
      table[suffixEnd] = prefixEnd;
      suffixEnd++;
    } else if (word[prefixEnd] !== word[suffixEnd] && prefixEnd !== 0) {
      // there's a mismatch, so we can't build a larger prefix
      // move the prefix to the position of the next largest prefix
      prefixEnd = table[prefixEnd - 1];
    } else {
      // we can't build a proper prefix with any of the proper suffixes
      // let's move on
      table[suffixEnd] = 0;
      suffixEnd++;
    }
  }

  return table;
}

function kmpSerach(long, short) {
  let table = matchTable(short);
  let shortIndex = 0;
  let longIndex = 0;
  let count = 0;
  while (longIndex < long.length - short.length + shortIndex + 1) {
    if (short[shortIndex] !== long[longIndex]) {
      // we found a mismatch
      // if we just started searching the short, move the long pointer
      // otherwise, move the short pointer to the end of the next potential prefix
      // that will lead to a match
      if (shortIndex === 0) longIndex++;
      else shortIndex = table[shortIndex - 1];
    } else {
      // we found a match! shift both pointers
      shortIndex++;
      longIndex++;
      // then check to see if we've found the substring in the large string
      if (shortIndex === short.length) {
        // we found a substring! increment the count
        // then move the short pointer to the end of the next potential prefix
        count++;
        shortIndex = table[shortIndex - 1];
      }
    }
  }

  return count;
}
