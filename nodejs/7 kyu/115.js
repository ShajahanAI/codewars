// https://www.codewars.com/kata/5c563cb78dac1951c2d60f01/train/javascript

// Passed

function passTheDoorMan(word) {
  let repeatedLetter;
  let idx = 0;
  for (letter of word.slice(1)) {
    if (letter == word[idx]) {
      repeatedLetter = letter;
      break;
    }

    idx++;
  }

  let alphabets = "abcdefghijklmnopqrstuvwxyz";
  let rightNumber = (alphabets.indexOf(repeatedLetter) + 1) * 3;
  return rightNumber;
}

const output = passTheDoorMan("apple");
console.log(output);