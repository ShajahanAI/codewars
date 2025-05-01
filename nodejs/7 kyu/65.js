// https://www.codewars.com/kata/5a32526ae1ce0ec0f10000b2/train/javascript

// Passed

function digitsAverage(input) {
  const digits = String(input)
    .split("")
    .map((digit) => Number(digit));
  if (digits.length === 1) return digits[0];

  const consecutiveAverages = digits
    .map((num, idx) => {
      if (idx == digits.length - 1) return null;

      const average = Math.ceil((num + digits[idx + 1]) / 2);
      return average;
    })
    .filter((value) => value !== null);

  const newInput = Number(
    consecutiveAverages.map((num) => String(num)).join("")
  );
  return digitsAverage(newInput);
}

const output = digitsAverage(246);
console.log(output);
