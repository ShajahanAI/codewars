// https://www.codewars.com/kata/59f061773e532d0c87000d16/train/javascript

// Passed

function elevatorDistance(array) {
  let consecutiveDifferences = array.map((num, idx) =>
    idx === array.length - 1 ? 0 : Math.abs(array[idx] - array[idx + 1])
  );
  let distance = consecutiveDifferences.reduce((prev, curr) => prev + curr, 0);
  return distance;
}

const output = elevatorDistance([5, 2, 8]);
console.log(output);