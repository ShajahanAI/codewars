// https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/javascript

// Passed

function bonusTime(salary, bonus) {
  let result = "£" + String(bonus ? salary * 10 : salary);
  return result;
}

const output = bonusTime(67890, true);
console.log(output);