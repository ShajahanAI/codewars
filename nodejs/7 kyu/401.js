// https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7/train/javascript

// Passed

function squaresNeeded(grains) {
  let result = grains !== 0 ? Math.floor(Math.log2(grains)) + 1 : 0;
  return result;
}

const output = squaresNeeded(3);
console.log(output);