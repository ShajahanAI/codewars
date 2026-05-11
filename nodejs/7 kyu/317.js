// https://www.codewars.com/kata/582f52208278c6be55000067/train/javascript

// Passed

function roundToFive(numbers) {
  let roundedNumbers = numbers.map((num) => 5 * Math.round(num / 5));
  return roundedNumbers;
}

const output = roundToFive([34.5, 56.2, 11, 13]);
console.log(output);