// https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7/train/javascript

// Passed

function kaprekarSplit(n) {
  let nSquare = n ** 2;
  let nSquareDigits = String(nSquare).split("");
  let result = -1;
  for (let splitIdx = 0; splitIdx <= nSquareDigits.length; splitIdx++) {
    let [num1, num2] = [
      nSquareDigits.slice(0, splitIdx + 1).join(""),
      nSquareDigits.slice(splitIdx + 1).join(""),
    ].map(Number);
    if (num1 + num2 === n) {
      result = nSquareDigits.length === 1 ? 0 : splitIdx + 1;
      break;
    }
  }
  return result;
}

const output = kaprekarSplit(5050);
console.log(output);