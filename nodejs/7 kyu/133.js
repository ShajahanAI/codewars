// https://www.codewars.com/kata/5574940eae1cf7d520000076/train/javascript

// Passed

function pattern(n) {
  if (n <= 0) return "";
  let numberStrings = [];
  let nearestOddNumber = n % 2 === 0 ? n - 1 : n;
  for (let num = 1; num <= nearestOddNumber; num += 2) {
    let numberString = String(String(num).repeat(num));
    numberStrings.push(numberString);
  }

  let result = numberStrings.join("\n");
  return result;
}

const output = pattern(4);
console.log(output);