// https://www.codewars.com/kata/583710ccaa6717322c000105/train/javascript

// Passed

function simpleMultiplication(number) {
  let result = number % 2 === 0 ? number * 8 : number * 9;
  return result;
}

const output = simpleMultiplication(8);
console.log(output);