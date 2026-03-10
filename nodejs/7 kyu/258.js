// https://www.codewars.com/kata/564f3d49a06556d27c000077/train/javascript

// Passed

function pattern(n) {
  let rows = [];
  for (let num = n; num >= 1; num--) {
    let digits = String(n - num + 1).split("");
    let digit = digits[digits.length - 1];

    let row = " ".repeat(n - num) + (" " + digit).repeat(num);
    rows.push(row);
  }

  let result = rows.join("\n");
  return result;
}

const output = pattern(12);
console.log(output);