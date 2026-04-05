// https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d/train/javascript

// Passed

function divisibleByLast(n) {
  let result = [false];
  let digits = String(n).split("");
  for (let idx = 0; idx < digits.length - 1; idx++) {
    let currDigit = Number(digits[idx]);
    let nextDigit = Number(digits[idx + 1]);

    if (currDigit !== 0 && nextDigit % currDigit === 0) {
      result.push(true);
    } else {
      result.push(false);
    }
  }

  return result;
}

const output = divisibleByLast(73312);
console.log(output);