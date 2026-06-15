// https://www.codewars.com/kata/5951d30ce99cf2467e000013/train/javascript

// Passed

function isPythagoreanTriple(integers) {
  let sortedIntegers = integers.sort((a, b) => a - b);
  let result =
    sortedIntegers[0] ** 2 + sortedIntegers[1] ** 2 === sortedIntegers[2] ** 2;
  return result;
}

const output = isPythagoreanTriple([3, 4, 5]);
console.log(output);