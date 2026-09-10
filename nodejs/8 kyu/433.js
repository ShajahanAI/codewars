// https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/javascript

// Passed

function powersOfTwo(n) {
  let result = [];
  for (let pow = 0; pow <= n; pow++) {
    result.push(2 ** pow);
  }
  return result;
}

const output = powersOfTwo(4);
console.log(output);