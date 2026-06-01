// https://www.codewars.com/kata/5612a42e746aa62de100001a/train/javascript

// Passed

function dBScale(intensity) {
  let decibels = 10 * Math.log10(intensity * 10 ** 12);
  return decibels;
}

const output = dBScale(0.00001);
console.log(output);