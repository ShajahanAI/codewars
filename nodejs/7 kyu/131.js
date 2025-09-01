// https://www.codewars.com/kata/58bccdf56f25ff6b6d00002f/train/javascript

// Passed

function rounding(n, m) {
  let bestFactor = Math.round(n / m);
  return ((2 * bestFactor - 1) * m) / 2 === n ? n : bestFactor * m;
}

const output = rounding(20, 3);
console.log(output);