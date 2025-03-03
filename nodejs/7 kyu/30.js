// https://www.codewars.com/kata/589422431a88082ea600002a/train/javascript

// Passed

function digitDegree(n) {
  let result = 0;
  while (String(n).length > 1) {
    result++;
    n = String(n)
      .split("")
      .reduce((a, b) => Number(a) + Number(b));
  }

  return result;
}

const output = digitDegree(547);
console.log(output);