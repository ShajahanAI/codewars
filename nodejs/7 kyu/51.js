// https://www.codewars.com/kata/59656c69253c365e58000046/train/javascript

// Passed

function maxPossibleScore(obj, arr) {
  const scores = Object.keys(obj).map((question) =>
    arr.includes(question) ? obj[question] * 2 : obj[question]
  );
  const totalScore = scores.reduce((prev, curr) => prev + curr, 0);
  return totalScore;
}

output = maxPossibleScore({ a: 1, b: 2, c: 4 }, ["a", "c"]);
console.log(output);
