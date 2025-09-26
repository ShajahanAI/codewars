// https://www.codewars.com/kata/593e978a3bb47a8308000b8f/train/javascript

// Passed

function rotateClockwise(matrix) {
  // basically, every row should become a column and vice versa
  if (matrix.length === 0) return [];

  let width = matrix[0].length;
  let rotatedMatrix = " "
    .repeat(width)
    .split("")
    .map((row) => row.trim());

  let matrixCopy = [...matrix];
  for (const row of matrixCopy.reverse()) {
    let currentIdx = 0;
    for (const char of row) {
      rotatedMatrix[currentIdx] += char;
      currentIdx++;
    }
  }

  return rotatedMatrix;
}

const output = rotateClockwise([
  "###.....",
  "..###...",
  "....###.",
  ".....###",
  ".....###",
  "....###.",
  "..###...",
  "###.....",
]);
console.log(output);