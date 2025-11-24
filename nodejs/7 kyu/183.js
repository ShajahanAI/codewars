// https://www.codewars.com/kata/55d7e5aa7b619a86ed000070/train/javascript

// Passed

function orderWord(s) {
  if (s === null || s.length === 0) return "Invalid String!";

  let characters = s.split("");
  let ascendingString = characters.sort().join("");
  return ascendingString;
}

const output = orderWord("Hello, World!");
console.log(output);