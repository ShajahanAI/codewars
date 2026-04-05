// https://www.codewars.com/kata/57b71a89b69bfc92c7000170/train/javascript

// Passed

function getNumberOfSquares(n) {
  let currBase = 0;
  let totalSum = 0;
  while (totalSum < n) {
    currBase++;
    totalSum += currBase ** 2;
  }

  currBase--;
  return currBase;
}

const output = getNumberOfSquares(15);
console.log(output);