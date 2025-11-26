// https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript

// Passed

function highAndLow(numbers) {
  let allNumbers = numbers.split(" ").map((strNum) => Number(strNum));
  let maximumNum = Math.max(...allNumbers);
  let minimumNum = Math.min(...allNumbers);
  let result = [maximumNum, minimumNum].join(" ");
  return result;
}

const output = highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4");
console.log(output);