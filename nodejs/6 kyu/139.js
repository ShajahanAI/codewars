// https://www.codewars.com/kata/553a2461098c64ae53000041/train/javascript

// Passed

function wordify(n) {
  const numToWordDict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
  };

  let strNum = String(n);
  let wordifiedNum = "";
  for (let idx = 0; idx < strNum.length; idx++) {
    let digit = strNum[idx];
    let word = numToWordDict[digit];
    if (strNum.length - idx === 3) {
      word += " hundred";
    } else if (Number(digit) === 0) {
      continue;
    } else if (strNum.length - idx == 2) {
      word = numToWordDict[Number(digit) * 10];

      if (Number(digit) === 1) {
        wordifiedNum += " " + numToWordDict[digit + strNum[idx + 1]];
        return wordifiedNum.trim();
      }
    }

    wordifiedNum += " " + word;
  }

  wordifiedNum = wordifiedNum.trim();
  return wordifiedNum;
}

const output = wordify(314);
console.log(output);