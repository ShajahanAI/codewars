// https://www.codewars.com/kata/59a1ec603203e862bb00004f/train/javascript

// Passed

function checkConcatenatedSum(originalNumber, n) {
  originalNumber = Math.abs(originalNumber);
  let digits = String(originalNumber).split("");
  let numbersMadeByConcatenation = digits.map((digitStr) =>
    Number(digitStr.repeat(n))
  );
  let hasProperty =
    numbersMadeByConcatenation.reduce((prev, curr) => prev + curr, 0) ===
    originalNumber;
  return hasProperty;
}

const output = checkConcatenatedSum(2997, 3);
console.log(output);