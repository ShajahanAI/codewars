// https://www.codewars.com/kata/566044325f8fddc1c000002c/train/javascript

// Passed

function evenChars(string) {
  if (string.length < 2 || string.length > 100) return "invalid string";

  let evenChars = [];
  for (let idx = 1; idx < string.length; idx += 2) {
    let char = string[idx];
    evenChars.push(char);
  }
  return evenChars;
}

const output = evenChars("abcdefghijklm");
console.log(output);