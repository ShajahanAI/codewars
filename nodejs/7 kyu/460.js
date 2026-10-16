// https://www.codewars.com/kata/555de49a04b7d1c13c00000e/train/javascript

// Passed

function add(...numbers) {
  let modifiedNumbers = numbers.map((num, idx) => num / (idx + 1));
  let result = modifiedNumbers.reduce((prev, curr) => prev + curr, 0);
  result = Math.round(result);
  return result;
}

const output = add(4, -3, -2);
console.log(output);