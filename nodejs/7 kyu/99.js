// https://www.codewars.com/kata/559d7951ce5e0da654000073/train/javascript

// Passed

function alternateSqSum(arr) {
  const square_sums = arr.map((num, idx) => (idx % 2 !== 0 ? num ** 2 : num));
  const result = square_sums.reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = alternateSqSum([1, 2, 3, 4, 5]);
console.log(output);