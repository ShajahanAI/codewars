// https://www.codewars.com/kata/58029cc9af749f80e3001e34/train/javascript

// Passed

function getNewNotes(salary, bills) {
  let remainingSalary = salary;
  for (const bill of bills) {
    remainingSalary -= bill;
  }

  remainingSalary = remainingSalary > 0 ? remainingSalary : 0;
  let fiveEuroBills = Math.floor(remainingSalary / 5);
  return fiveEuroBills;
}

const output = getNewNotes(2000, [500, 160, 400]);
console.log(output);