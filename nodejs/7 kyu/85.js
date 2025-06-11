// https://www.codewars.com/kata/5a995c2aba1bb57f660001fd/train/javascript

// Passed

function scrollingText(text) {
  text = text.toUpperCase();
  const rotatedTexts = text
    .split("")
    .map((char, idx) => text.slice(idx).concat(text.slice(0, idx)));
  return rotatedTexts;
}

const output = scrollingText("codewars");
console.log(output);