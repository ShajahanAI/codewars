// https://www.codewars.com/kata/6965d769930fb2eff921668f/train/javascript

// Passed

function solution(first, second) {
  while (first >= second - first) {
    [second, first] = [first, second - first];
  }

  let result = [first, second];
  return result;
}

const output = solution(398, 644);
console.log(output);