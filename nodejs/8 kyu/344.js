// https://www.codewars.com/kata/57eae65a4321032ce000002d/train/javascript

// Passed

function fakeBin(x) {
  let result = x
    .split("")
    .map((digit) => (Number(digit) < 5 ? "0" : "1"))
    .join("");
  return result;
}

const output = fakeBin("509321967506747");
console.log(output);