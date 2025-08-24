// https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/javascript

// Passed

function longestWord(stringOfWords) {
  let maximumLength = 0;
  let maximumLengthWord = null;
  for (const word of stringOfWords.split(" ")) {
    if (word.length >= maximumLength) {
      maximumLengthWord = word;
      maximumLength = word.length;
    }
  }

  return maximumLengthWord;
}

const output = longestWord("red blue grey");
console.log(output);