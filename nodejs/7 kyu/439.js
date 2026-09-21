// https://www.codewars.com/kata/594adadee075005308000122/train/javascript

// Passed

function evenAndOdd(num) {
  let digits = String(num)
    .split("")
    .map((strDigit) => Number(strDigit));
  let [evenStrNum, oddStrNum] = ["", ""];
  for (const digit of digits) {
    if (digit % 2 === 0) {
      evenStrNum += String(digit);
    } else {
      oddStrNum += String(digit);
    }
  }

  let [evenNum, oddNum] = [Number(evenStrNum), Number(oddStrNum)];
  let result = [evenNum, oddNum];
  return result;
}

const output = evenAndOdd(126453);
console.log(output);