// https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/javascript

// Passed

function removeConsecutiveDuplicates(string) {
  let wordsToJoin = [];
  let lastWord;
  for (const word of string.split(" ")) {
    if (word === lastWord) {
      continue;
    }

    lastWord = word;
    wordsToJoin.push(lastWord);
  }

  let result = wordsToJoin.join(" ");
  return result;
}

const output = removeConsecutiveDuplicates(
  "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta",
);
console.log(output);