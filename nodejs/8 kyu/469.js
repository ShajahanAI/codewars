// https://www.codewars.com/kata/6ad649de715eb5f5359a7e62/train/javascript

// Passed

function batteryBars(percent) {
  let number = Math.floor(percent / 20);
  let result = "[" + "#".repeat(number) + ".".repeat(5 - number) + "]";
  return result;
}

const output = batteryBars(100);
console.log(output);