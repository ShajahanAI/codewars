// https://www.codewars.com/kata/55466644b5d240d1d70000ba/train/javascript

// Passed

function candies(kids) {
  if (kids.length === 1 || kids.length === 0) {
    return -1;
  }

  let maxCandies = Math.max(...kids);
  let candiesToHandOut = kids.map((candyCount) => maxCandies - candyCount);
  let totalCandiesToHandOut = candiesToHandOut.reduce(
    (prev, curr) => prev + curr,
    0,
  );
  return totalCandiesToHandOut;
}

const output = candies([5, 8, 6, 4]);
console.log(output);