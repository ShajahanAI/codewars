// https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/javascript

// Passed

function toCsvText(array) {
  let rows = array.map((arr) => arr.join(","));
  let result = rows.join("\n");
  return result;
}

const output = toCsvText([
  [0, 1, 2, 3, 45],
  [10, 11, 12, 13, 14],
  [20, 21, 22, 23, 24],
  [30, 31, 32, 33, 34],
]);
console.log(output);