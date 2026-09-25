// https://www.codewars.com/kata/5a2e8c0955519e54bf0000bd/train/javascript

// Passed

function checkDigit(number, index1, index2, digit) {
  let [startIdx, endIdx] = [index1, index2].sort((a, b) => a - b);
  let slicedNumber = String(number).slice(startIdx, endIdx + 1);
  let digitsToCheck = new Set(slicedNumber);
  let result = digitsToCheck.has(String(digit));
  return result;
}

const output = checkDigit(67845123654, 4, 2, 4);
console.log(output);