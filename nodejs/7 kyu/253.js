// https://www.codewars.com/kata/59a8570b570190d313000037/train/javascript

// Passed

function sumCubes(n) {
  let totalSum = 0;
  for (let num = 1; num <= n; num++) {
    totalSum += num ** 3;
  }

  return totalSum;
}

const output = sumCubes(10);
console.log(output);