// https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/javascript

// Passed

function addLength(str) {
  let words = str.split(" ");
  let modifiedArr = words.map((word) => word + " " + String(word.length));
  return modifiedArr;
}

const output = addLength("apple ban");
console.log(output);