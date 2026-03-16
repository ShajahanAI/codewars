// https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/javascript

// Passed

function maps(x) {
  let mappedArr = x.map((val) => val * 2);
  return mappedArr;
}

const output = maps([4, 1, 1, 1, 4]);
console.log(output);