// https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/javascript

// Passed 

function cubeOdd(arr) {
  if (!arr.every((elem) => typeof elem == "number")) return undefined;

  const oddCubicSum = arr
    .filter((num) => (num > 0 ? num : -num) % 2 === 1)
    .map((num) => num ** 3)
    .reduce((prev, curr) => prev + curr, 0);
  return oddCubicSum;
}

const output = cubeOdd([1, 2, 3, 4]);
console.log(output);