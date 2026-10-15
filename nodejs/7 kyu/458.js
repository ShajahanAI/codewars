// https://www.codewars.com/kata/55d2aee99f30dbbf8b000001/train/javascript

// Passed

function scoreTest(str, right, omit, wrong) {
  let result = 0;
  for (const answerType of str) {
    if (answerType === 0) {
      result += right;
    } else if (answerType === 1) {
      result += omit;
    } else if (answerType === 2) {
      result -= wrong;
    }
  }

  return result;
}

const output = scoreTest([0, 0, 0, 0, 2, 1, 0], 2, 0, 1);
console.log(output);