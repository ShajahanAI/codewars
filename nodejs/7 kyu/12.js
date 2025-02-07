// https://www.codewars.com/kata/59564f3bcc15b5591a00004a/train/javascript

// Passed

function filterEvenLengthWords(words) {
    return words.filter((word) => word.length % 2 === 0);
  }

let output = filterEvenLengthWords(['One', 'Four', 'Three']);
console.log(output);