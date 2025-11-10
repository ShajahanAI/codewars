// https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1/train/javascript

// Passed

function isKiss(words) {
  let allWords = words.split(" ");
  let totalWords = allWords.length;
  let isSimple = allWords.every((word) => word.length <= totalWords);
  let result = isSimple ? "Good work Joe!" : "Keep It Simple Stupid";
  return result;
}

const output = isKiss("Joe had a bad day");
console.log(output);