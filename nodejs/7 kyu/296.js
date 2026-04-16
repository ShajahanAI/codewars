// https://www.codewars.com/kata/59aa2cccd0a5ffdfa000005b/train/javascript

// Passed

function globalEstimate(estimates) {
  let [bestCase, worstCase] = [0, 0];
  for (const estimate of estimates) {
    bestCase += estimate[0];
    worstCase += estimate[1];
  }
  let averageCase = (bestCase + worstCase) / 2;
  let result = [bestCase, averageCase, worstCase];
  return result;
}

const output = globalEstimate([
  [1, 3],
  [1, 4],
  [1, 5],
]);
console.log(output);