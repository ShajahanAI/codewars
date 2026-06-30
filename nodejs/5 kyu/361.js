// https://www.codewars.com/kata/5632e12703e2037fa7000061/train/javascript

// Passed

function base64toBase10(base64) {
  let base64CharToValMap = new Object();
  let base64Characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  for (let idx = 0; idx < base64Characters.length; idx++) {
    let base64Char = base64Characters[idx];
    base64CharToValMap[base64Char] = idx;
  }

  let result = 0;
  for (let idx = 0; idx < base64.length; idx++) {
    let base64Char = base64[idx];
    let val = base64CharToValMap[base64Char];
    let pow = base64.length - idx - 1;
    result += val * 64 ** pow;
  }

  return result;
}

const output = base64toBase10("WIN");
console.log(output);