// https://www.codewars.com/kata/59c6fa6972851e8959000067/train/javascript

// Passed

function ìsZeroBalanced(n) {
  const sum = n.reduce((prev, curr) => prev + curr, 0);
  const isZeroBalanced = n.length
    ? n.every((number) => sum == 0 && n.indexOf(-1 * number) !== -1)
    : false;
  return isZeroBalanced;
}

const output = ìsZeroBalanced([3, -3, 5, -5, 7, -7]);
console.log(output);