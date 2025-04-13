// https://www.codewars.com/kata/5e4217e476126b000170489b/train/javascript

// Passed

function polydivisible(x) {
  const digits = String(x).split("");
  const numbers = digits.map((value, idx) => digits.slice(0, idx + 1).join(""));
  const isPolyDivisible = numbers.every(
    (number, idx) => number % (idx + 1) === 0
  );
  return isPolyDivisible;
}

const output = polydivisible(123);
console.log(output);
