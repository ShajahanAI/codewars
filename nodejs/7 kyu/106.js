// https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/javascript

// Passed

function solve(a) {
  let oddCount = 0;
  let evenCount = 0;
  for (const elem of a) {
    if (typeof elem === "number") {
      if (elem % 2 === 0) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }

  let evenOddDisparity = evenCount - oddCount;
  return evenOddDisparity;
}

const output = solve([
  5,
  15,
  16,
  10,
  6,
  4,
  16,
  "t",
  13,
  "n",
  14,
  "k",
  "n",
  0,
  "q",
  "d",
  7,
  9,
]);
console.log(output);