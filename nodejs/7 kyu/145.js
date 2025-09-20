// https://www.codewars.com/kata/59cd0535328801336e000649/train/javascript

// Passed

function interest(p, r, n) {
  let totalUnderSimpleInterest = p * (1 + r * n);
  let totalUnderCompoundInterest = p * (1 + r) ** n;

  let result = [
    Math.round(totalUnderSimpleInterest),
    Math.round(totalUnderCompoundInterest),
  ];
  return result;
}
const output = interest(100, 0.1, 2);
console.log(output);