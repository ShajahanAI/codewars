// https://www.codewars.com/kata/56644a421b7c94c622000056/train/javascript

// Passed

function mostLikely(prob1, prob2) {
  let probToValue = (prob) => {
    let [numerator, denominator] = prob.split(":").map(Number);
    let value = numerator / denominator;
    return value;
  };

  let result = probToValue(prob1) > probToValue(prob2);
  return result;
}

const output = mostLikely("1:3", "1:2");
console.log(output);