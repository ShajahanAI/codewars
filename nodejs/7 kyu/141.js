// https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/javascript

// Passed

function minMinMax(array) {
  let minNum = Math.min(...array);
  let maxNum = Math.max(...array);
  let minAbsent;
  for (let num = minNum; num < maxNum; num++) {
    if (!array.includes(num)) {
      minAbsent = num;
      break;
    }
  }

  let result = [minNum, minAbsent, maxNum];
  return result;
}

const output = minMinMax([-1, 4, 5, -23, 24]);
console.log(output);
