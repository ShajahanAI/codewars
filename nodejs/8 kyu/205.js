// https://www.codewars.com/kata/515e271a311df0350d00000f/train/javascript

// Passed

function squareSum(numbers) {
  let numbersSquared = numbers.map((num) => num ** 2);
  let sumOfNumbersSquared = numbersSquared.reduce(
    (prev, curr) => prev + curr,
    0
  );
  return sumOfNumbersSquared;
}

const output = squareSum([1, 2]);
console.log(output);