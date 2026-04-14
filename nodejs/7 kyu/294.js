// https://www.codewars.com/kata/5ef0456fcd067000321baffa/train/javascript

// Passed

function connotation(str) {
  let words = str.split(" ").filter((word) => word.length > 0);
  let wordsSide = words.map((word) =>
    word.toLowerCase()[0].charCodeAt() <= 109 ? 1 : -1,
  ); // arr of 1 or -1
  let overallSide = wordsSide.reduce((a, b) => a + b, 0);
  let result = overallSide >= 0;
  return result;
}

const output = connotation("CHOCOLATE MAKES A GREAT SNACK");
console.log(output);