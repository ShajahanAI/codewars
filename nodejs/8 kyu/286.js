// https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/javascript

// Passed

function squareArea(A) {
  let side = (2 * A) / Math.PI;
  let area = Math.round(side ** 2 * 100) / 100;
  return area;
}

const output = squareArea(2);
console.log(output);