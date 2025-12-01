// https://www.codewars.com/kata/5511b2f550906349a70004e1/train/javascript

// Passed

function lastDigit(n, m) {
  if (Number(m) === 0) {
    return 1n; // n ^ 0 = 1
  }

  let digitToLastDigitPatternMap = {
    0: "0000",
    1: "1111",
    2: "2486",
    3: "3971",
    4: "4646",
    5: "5555",
    6: "6666",
    7: "7931",
    8: "8426",
    9: "9191",
  };

  let lastDigit = String(n)[String(n).length - 1];
  let lastDigitPattern = digitToLastDigitPatternMap[lastDigit];
  let lastDigitOfPowerIdx =
    BigInt(m) % 4n === 0n ? 3 : Number((BigInt(m) % 4n) - 1n);
  let lastDigitOfPower = BigInt(lastDigitPattern[lastDigitOfPowerIdx]);
  return lastDigitOfPower;
}

const output = lastDigit(
  1606938044258990275541962092341162602522202993782792835301376n,
  2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376n
);
console.log(output);