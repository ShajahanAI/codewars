// https://www.codewars.com/kata/54557d61126a00423b000a45/train/javascript

// Passed

function shorterReverseLonger(a, b) {
  let longerString = b.length > a.length ? b : a;
  let shorterString = longerString === a ? b : a;
  let result =
    shorterString + longerString.split("").reverse().join("") + shorterString;
  return result;
}

const output = shorterReverseLonger("first", "abcde");
console.log(output);