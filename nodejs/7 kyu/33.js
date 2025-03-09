// https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/javascript

// Passed

function differenceOfSquares(n) {
  const numbersTillN = [];
  for (let i = 0; i < n; i++) {
    numbersTillN.push(i + 1);
  }

  return (
    Math.pow(
      numbersTillN.reduce((prev, curr) => prev + curr, 0),
      2
    ) -
    numbersTillN
      .map((num) => Math.pow(num, 2))
      .reduce((prev, curr) => prev + curr, 0)
  );
}

const output = differenceOfSquares(10);
console.log(output);
