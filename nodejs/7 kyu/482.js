// https://www.codewars.com/kata/5654d2428be803670a000030/train/javascript

// Passed

function guessMyNumber(guess, number = "123-451-2345") {
  let allDigitsSet = new Set("0123456789");
  let digitsToReplace = allDigitsSet.difference(new Set(guess));
  let result = number;
  for (const digitToReplace of digitsToReplace) {
    result = result.replaceAll(digitToReplace, "#");
  }

  return result;
}

const output = guessMyNumber("052", "123-451-2345");
console.log(output);