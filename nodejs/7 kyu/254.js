// https://www.codewars.com/kata/559590633066759614000063/train/javascript

// Passed

function minMax(arr) {
  let buyPrice = Math.min(...arr);
  let sellPrice = Math.max(...arr);
  let result = [buyPrice, sellPrice];
  return result;
}

const output = minMax([1, 2, 3, 4, 5]);
console.log(output);