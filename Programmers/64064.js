function solution(user_id, banned_id) {
  const set = new Set();
  const regEx = banned_id.map(
    (id) => new RegExp(`^${id.replaceAll("*", ".")}$`)
  );
  const selected = Array(user_id.length).fill(false);

  const dfs = (index, arr) => {
    if (index === banned_id.length) {
      set.add(arr.sort().join(","));
    } else {
      for (let i = 0; i < user_id.length; i++) {
        if (selected[i]) {
          continue;
        }

        if (user_id[i].match(regEx[index])) {
          selected[i] = true;
          dfs(index + 1, [...arr, user_id[i]]);
          selected[i] = false;
        }
      }
    }
  };

  dfs(0, []);

  return set.size;
}
