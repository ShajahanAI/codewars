// https://www.codewars.com/kata/59b11f57f322e5da45000254/train/javascript

// Passed

function onesComplement(n) {
  let complement = n
    .split("")
    .map((ch) => (ch === "1" ? "0" : "1"))
    .join("");
  return complement;
}

const output = onesComplement("1101");
console.log(output);