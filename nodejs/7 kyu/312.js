// https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/javascript

// Passed

function sumOfN(n) {
  let result = [];
  let sum = 0;
  let isNegative = n < 0;
  for (let i = 0; i < Math.abs(n) + 1; i++) {
    sum += i;
    result.push(sum * (isNegative ? -1 : 1));
  }

  return result;
}

const output = sumOfN(3);
console.log(output);