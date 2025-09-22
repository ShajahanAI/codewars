// https://www.codewars.com/kata/57882daf90b2f375280000ad/train/javascript

// Passed

function SumSquares(l) {
  let computeSquares = (arr) => {
    let squares = [];
    for (const possibleNum of arr) {
      if (typeof possibleNum === "number") {
        squares.push(possibleNum ** 2);
      } else {
        squares.push(...computeSquares(possibleNum));
      }
    }
    return squares;
  };

  let computedSquares = computeSquares(l);
  let sumOfSquares = computedSquares.reduce((prev, curr) => prev + curr, 0);
  return sumOfSquares;
}

const output = SumSquares([1, [[3], 10, 5, [2, [3], [4], [5, [6]]]], [10]]);
console.log(output);