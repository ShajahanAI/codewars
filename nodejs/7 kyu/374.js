// https://www.codewars.com/kata/5a0efbb7c374cb69970000cf/train/javascript

// Passed

function reverseMessage(str) {
  let result = "";
  if (str.length !== 0) {
    let words = str.split(" ");
    let toTitleCase = (word) =>
      word[0].toUpperCase() + word.slice(1).toLowerCase();
    let wordsToJoin = words
      .reverse()
      .map((word) => toTitleCase(word.split("").reverse().join("")));
    result = wordsToJoin.join(" ");
  }
  return result;
}

const output = reverseMessage("Reverse this message!");
console.log(output);