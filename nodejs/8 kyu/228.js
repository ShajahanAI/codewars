// https://www.codewars.com/kata/5966e33c4e686b508700002d/train/javascript

// Passed

function sumStr(a, b) {
  let result = Number(a) + Number(b);
  let resultStr = String(result);
  return resultStr;
}

const output = sumStr("34", "5");
console.log(output);