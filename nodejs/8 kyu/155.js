// https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/javascript

// Passed

function reverseWords(str) {
  return str.split(" ").reverse().join(" ");
}

const output = reverseWords("yoda doesn't speak like this");
console.log(output);