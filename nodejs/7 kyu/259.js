// https://www.codewars.com/kata/5a05fe8a06d5b6208e00010b/train/javascript

// Passed

function seqToOne(n) {
  let sequenceArr = [];
  let currentNum = n;
  while (currentNum !== 1) {
    sequenceArr.push(currentNum);
    currentNum = currentNum < 1 ? currentNum + 1 : currentNum - 1;
  }

  sequenceArr.push(currentNum);

  return sequenceArr;
}

const output = seqToOne(100);
console.log(output);