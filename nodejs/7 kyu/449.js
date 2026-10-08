// https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/train/javascript

// Passed

function isItLetter(character) {
  let result = RegExp("[a-zA-Z]").test(character);
  return result;
}

const output = isItLetter("a");
console.log(output);