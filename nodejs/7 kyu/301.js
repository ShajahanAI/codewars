// https://www.codewars.com/kata/56b0f6243196b9d42d000034/train/javascript

// Passed

function sumFactorial(arr) {
  let numToFactorialMap = new Object();
  let calcFactorial = (num) => {
    if (num === 1) {
      return 1;
    }

    let factorial =
      num in numToFactorialMap
        ? numToFactorialMap[num]
        : num * calcFactorial(num - 1);
    numToFactorialMap[num] = factorial;
    return factorial;
  };

  let totalSum = 0;
  for (const num of arr) {
    let numFactorial = calcFactorial(num);
    totalSum += numFactorial;
  }

  return totalSum;
}

const output = sumFactorial([4, 6]);
console.log(output);