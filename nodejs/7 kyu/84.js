// https://www.codewars.com/kata/59b710ed70a3b7dd8f000027/train/javascript

// Passed

function isAllPossibilities(x) {
  const allPossibilitiesArray = x.map((num, idx) => idx);
  return allPossibilitiesArray.every((num) => x.includes(num));
}

const output = isAllPossibilities([1, 2, 0, 3]);
console.log(output);