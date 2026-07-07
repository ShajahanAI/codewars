// https://www.codewars.com/kata/5888514674b58e929a000036/train/javascript

// Passed

function decipher(cipher) {
  let characterCodes = [];
  let currentNumberStr = String();
  for (const digit of cipher) {
    currentNumberStr += digit;
    let currentNumber = Number(currentNumberStr);
    if (currentNumber >= 97 && currentNumber <= 122) {
      characterCodes.push(currentNumber);
      currentNumberStr = String();
    }
  }

  let result = characterCodes.map((code) => String.fromCharCode(code)).join("");
  return result;
}

const output = decipher("10197115121");
console.log(output);