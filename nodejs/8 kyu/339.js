// https://www.codewars.com/kata/56b29582461215098d00000f/train/javascript

// Passed

function pipeFix(numbers) {
  let minNumber = numbers[0];
  let maxNumber = numbers[numbers.length - 1];
  let result = [];
  for (let num = minNumber; num <= maxNumber; num++) {
    result.push(num);
  }

  return result;
}

const output = pipeFix([1, 2, 3, 12]);
console.log(output);