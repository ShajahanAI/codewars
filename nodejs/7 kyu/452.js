// https://www.codewars.com/kata/5723b111101f5f905f0000a5/train/javascript

// Passed

function resistor_parallel(...resistances) {
  let denominator = resistances
    .map((resistance) => 1 / resistance)
    .reduce((prev, curr) => prev + curr, 0);
  let result = 1 / denominator;
  return result;
}

const output = resistor_parallel(20, 20, 40);
console.log(output);