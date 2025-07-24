// https://www.codewars.com/kata/5822d89270ca28c85c0000f3/train/javascript

// Passed

function scramble(str, arr) {
  let indexCharMap = new Object();
  arr.forEach((charPosition, stringIndex) => {
    indexCharMap[charPosition] = str[stringIndex];
  });

  let result = "";
  for (let idx = 0; idx < str.length; idx++) {
    result += indexCharMap[idx];
  }

  return result;
}

const output = scramble("abcd", [0, 3, 1, 2]);
console.log(output);