// https://www.codewars.com/kata/589478160c0f8a40870000bc/train/javascript

// Paased

function arrowArea(a, b) {
  let rectangleArea = a * b;
  let arrowArea = rectangleArea / 4;
  return arrowArea;
}

const output = arrowArea(4, 2);
console.log(output);