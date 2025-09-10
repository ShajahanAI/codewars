// https://www.codewars.com/kata/563b1f55a5f2079dc100008a/train/javascript

// Passed

function getLargerNumbers(a, b) {
  let comparedArray = a.map((num, idx) => (num >= b[idx] ? num : b[idx]));
  return comparedArray;
}

const output = getLargerNumbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]);
console.log(output);