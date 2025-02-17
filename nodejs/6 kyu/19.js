// https://www.codewars.com/kata/5264d2b162488dc400000001/train/javascript

// Passed

function spinWords(string) {
  const words = string.split(" ");
  return words
    .map((word) => (word.length >= 5 ? word.split("").reverse().join("") : word))
    .join(" ");
}

const output = spinWords('Hey fellow warriors');
console.log(output);