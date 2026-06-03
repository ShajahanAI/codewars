// https://www.codewars.com/kata/5d50e3914861a500121e1958/train/javascript

// Passed

function addLetters(...letters) {
  let allLetters = "abcdefghijklmnopqrstuvwxyz";
  let letterToValueMap = new Object();
  let valueToLetterMap = new Object();
  let value = 0;
  for (const letter of allLetters) {
    value++;
    letterToValueMap[letter] = value;
    valueToLetterMap[value] = letter;
  }

  let key =
    letters
      .map((letter) => letterToValueMap[letter])
      .reduce((prev, curr) => prev + curr, 0) % 26;
  key = key === 0 ? 26 : key;
  let result = valueToLetterMap[key];
  return result;
}

const output = addLetters("a", "b", "c");
console.log(output);