// https://www.codewars.com/kata/51edd51599a189fe7f000015/train/javascript

// Passed

var solution = function (firstArray, secondArray) {
  let meanSquareArray = firstArray.map(
    (num, idx) => (num - secondArray[idx]) ** 2
  );
  let meanSquareError =
    meanSquareArray.reduce((prev, curr) => prev + curr, 0) /
    meanSquareArray.length;
  return meanSquareError;
};

const output = solution([1,2,3],[4,5,6]);
console.log(output);