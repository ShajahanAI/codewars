// https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/javascript

// Passed

function roundToNext5(n) {
  let remainder = n % 5;
  let result = remainder === 0 ? n : 5 * Math.ceil(n / 5);
  return result;
}

const output = roundToNext5(3);
console.log(output);