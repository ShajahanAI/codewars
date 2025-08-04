// https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/javascript

// Passed

function between(a, b) {
  let result = [];
  for (let i = a; i <= b; i++) {
    result.push(i);
  }

  return result;
}

const output = between(1, 4);
console.log(output);