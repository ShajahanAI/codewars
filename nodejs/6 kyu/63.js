// https://www.codewars.com/kata/5a91e0793e9156ccb0003f6e/train/javascript

// Passed

const matrixfy = (str) => {
  if (!str.length) return "name must be at least one letter";
  if (str.length == 1) return [[str]];
  const nearestNumberToSquare = Math.ceil(Math.log2(str.length));
  const nearestSquareNumber = 2 ** nearestNumberToSquare;
  str = str + ".".repeat(nearestSquareNumber - str.length + 1);
  const matrix = [];
  for (let idx = 0; idx < nearestSquareNumber; idx += nearestNumberToSquare) {
    const row = str.slice(idx, idx + nearestNumberToSquare).split("");
    matrix.push(row);
  }
  return matrix;
};

const output = matrixfy("Franklin");
console.log(output);