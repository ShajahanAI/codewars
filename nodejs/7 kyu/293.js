// https://www.codewars.com/kata/58067088c27998b119000451/train/javascript

// Passed

function reverseFactorial(num) {
  let factorialNum = 1;
  let factorialVal = 1;
  while (factorialVal < num) {
    factorialNum++;
    factorialVal *= factorialNum;
  }

  factorialNum = factorialVal === num ? `${factorialNum}!` : "None";
  return factorialNum;
}

const output = reverseFactorial(120);
console.log(output);