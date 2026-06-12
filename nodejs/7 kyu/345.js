// https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/javascript

// Passed

function sumEvenNumbers(input) {
  let evenNumbers = input.filter((num) => num % 2 === 0);
  let result = evenNumbers.reduce((prev, curr) => prev + curr, 0);
  return result;
}

const output = sumEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
console.log(output);