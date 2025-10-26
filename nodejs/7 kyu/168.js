// https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/javascript

// Passed

function sortGiftCode(code) {
  let sortedLetters = code.split("").sort();
  let sortedGiftCode = sortedLetters.join("");
  return sortedGiftCode;
}

const output = sortGiftCode("pqksuvy");
console.log(output);