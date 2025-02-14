// https://www.codewars.com/kata/5b043e3886d0752685000009/train/javascript

// Passed

function michaelPays(costs) {
  if (costs < 5) {
    return Number(costs.toFixed(2)); // Michael pays for the full pizza
  }

  const michaelsContribution = (1 / 3) * costs <= 10 ? (2 / 3) * costs : costs - 10;
  return Number(michaelsContribution.toFixed(2));
}

const output = michaelPays(4.325);
console.log(output);
