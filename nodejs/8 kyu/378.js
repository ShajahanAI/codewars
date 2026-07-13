// https://www.codewars.com/kata/5865918c6b569962950002a1/train/javascript

// Passed

function strCount(str, letter) {
  let result = str.split("").filter((char) => char === letter).length;
  return result;
}

const output = strCount("Hello", "o");
console.log(output);