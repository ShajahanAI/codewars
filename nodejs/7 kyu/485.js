// https://www.codewars.com/kata/670550a8fc404105769b06be/train/javascript

// Passed

function qf(donations, pool) {
  // calculating weights
  let weights = [];
  let totalWeight = 0;
  for (const donationsArr of donations) {
    let weight =
      donationsArr
        .map((donation) => donation ** 0.5)
        .reduce((prev, curr) => prev + curr) ** 2;
    totalWeight += weight;
    weights.push(weight);
  }

  // calculating funding
  let result = [];
  for (const weight of weights) {
    let funding = Math.round((weight / totalWeight) * pool);
    result.push(funding);
  }

  return result;
}

const output = qf([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10]], 20);
console.log(output);