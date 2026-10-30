// https://www.codewars.com/kata/5641a03210e973055a00000d/train/javascript

// Passed

function twoDecimalPlaces(n) {
  let result = Math.round(n * 100) / 100;
  return result;
}

const output = twoDecimalPlaces(4.659725356);
console.log(output);