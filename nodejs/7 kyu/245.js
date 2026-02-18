// https://www.codewars.com/kata/5890579a34a7d44f3b00009e/train/javascript

// Passed

function manipulate(num) {
  num = String(num);
  let idxToSplit = Math.floor(num.length / 2);
  let manipulatedNum = Number(
    num.slice(0, idxToSplit) + "0".repeat(num.length - idxToSplit),
  );
  return manipulatedNum;
}

const output = manipulate(192827764920);
console.log(output);