// https://www.codewars.com/kata/59a9919107157a45220000e1/train/javascript

// Passed

function findAll(array, n) {
  let allIndexes = array
    .map((val, idx) => (val === n ? idx : null))
    .filter((val) => val !== null);
  return allIndexes;
}

const output = findAll(
  [20, 20, 10, 13, 15, 2, 7, 2, 20, 3, 18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5],
  20,
);
console.log(output);