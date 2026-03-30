// https://www.codewars.com/kata/5299413901337c637e000004/train/javascript

// Passed

function getMissingElement(superImportantArray) {
  let digits = new Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
  for (const digit of superImportantArray) {
    digits.delete(digit);
  }

  let missingDigit = Array.from(digits)[0];
  return missingDigit;
}

const output = getMissingElement([0, 5, 1, 3, 2, 9, 7, 6, 4]);
console.log(output);