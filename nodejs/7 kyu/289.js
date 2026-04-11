// https://www.codewars.com/kata/6512b3775bf8500baea77663/train/javascript

// Passed

function gimmeTheLetters(sp) {
  let allLetters = "abcdefghijklmnopqrstuvwxyz";
  let letterToIndexMap = new Object();
  let indexToLetterMap = new Object();

  let idx = 0;
  for (const letter of allLetters) {
    letterToIndexMap[letter] = idx;
    indexToLetterMap[idx] = letter;
    idx++;
  }

  let sequence = "";
  let [startLetter, endLetter] = sp.split("-");
  let startIdx = letterToIndexMap[startLetter.toLowerCase()];
  let endIdx = letterToIndexMap[endLetter.toLowerCase()];
  let uppercaseLetter = startLetter === startLetter.toUpperCase();

  for (let idx = startIdx; idx <= endIdx; idx++) {
    sequence += uppercaseLetter
      ? indexToLetterMap[idx].toUpperCase()
      : indexToLetterMap[idx];
  }

  return sequence;
}

const output = gimmeTheLetters("C-R");
console.log(output);