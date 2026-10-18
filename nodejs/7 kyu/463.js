// https://www.codewars.com/kata/5900750cb7c6172207000054/train/javascript

// Passed

function stickyCalc(operation, val1, val2) {
  let operationToFunctionMap = {
    "+": (num1, num2) => num1 + num2,
    "-": (num1, num2) => num1 - num2,
    "*": (num1, num2) => num1 * num2,
    "/": (num1, num2) => num1 / num2,
  };

  let operationFunction = operationToFunctionMap[operation];

  [val1, val2] = [val1, val2].map(Math.round);
  let num1 = Number(String(val1) + String(val2));
  let num2 = val2;

  let result = Math.round(operationFunction(num1, num2));
  return result;
}

const output = stickyCalc("+", 4.2, 7);
console.log(output);