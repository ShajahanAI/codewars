// https://www.codewars.com/kata/5983cba828b2f1fd55000114/train/javascript

// Passed

function oddOne(arr) {
  let result = -1;
  let currentIdx = 0;
  for (const num of arr) {
    if (Math.abs(num) % 2 === 1) {
      result = currentIdx;
      break;
    }

    currentIdx++;
  }

  return result;
}

const output = oddOne([4, -8, 98, -12, -7, 90, 100]);
console.log(output);