/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = new Map()

    strs.forEach((s) => {
        let sorted = s.split('').sort().join('')
        if (map.has(sorted)) {
            map.set(sorted, [s, ...map.get(sorted)])
        }
        else map.set(sorted, [s])
    })

    return Array.from(map.values())
};
