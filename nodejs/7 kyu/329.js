// https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/javascript

// Passed

function seven(m) {
  let currentStepNumber = m;
  let stepsCount = 0;
  let digits = String(currentStepNumber).split("");

  while (digits.length > 2) {
    let [x, y] = [
      Number(digits.slice(0, digits.length - 1).join("")),
      Number(digits[digits.length - 1]),
    ];
    currentStepNumber = x - 2 * y;
    digits = String(currentStepNumber).split("");
    stepsCount++;
  }

  let result = [currentStepNumber, stepsCount];
  return result;
}

const output = seven(1021);
console.log(output);