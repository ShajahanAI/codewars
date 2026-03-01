// https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/javascript

// Passed

function rowWeights(array) {
  let teamWeights = [0, 0];
  let currentIdx = 0;
  for (const weight of array) {
    teamWeights[currentIdx % 2] += weight;
    currentIdx++;
  }

  return teamWeights;
}

const output = rowWeights([29, 83, 67, 53, 19, 28, 96]);
console.log(output);