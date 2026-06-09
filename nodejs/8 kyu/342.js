// https://www.codewars.com/kata/56b1f01c247c01db92000076/train/javascript

// Passed

function doubleChar(str) {
  let characters = str.split("");
  let result = characters.map((char) => char + char).join("");
  return result;
}

const output = doubleChar("abcd");
console.log(output);