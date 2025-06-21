// https://www.codewars.com/kata/54b81566cd7f51408300022d/train/javascript

// Passed

function wordSearch(query, seq) {
  const partialWords = seq.filter((word) =>
    word.toLowerCase().includes(query.toLowerCase())
  );
  const result = partialWords.length > 0 ? partialWords : ["Empty"];
  return result;
}

const output = wordSearch("ab", ["za", "ab", "abc", "zab", "zbc"]);
console.log(output);