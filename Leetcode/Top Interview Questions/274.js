/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    let answer = 0

    citations.sort((a, b) => b - a)
    
    for (let i = 0; i < citations.length; i++) {
        if (i + 1 >= citations[i]) {
            answer = Math.max(answer, citations[i])
        } else {
            answer = Math.min(i + 1, citations[i])
        }
    }
    return answer
};
