// https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/train/javascript

// Passed

function calculate(a, operator, b) {
  let result = null;
  if (operator === "+") {
    result = a + b;
  } else if (operator === "-") {
    result = a - b;
  } else if (operator === "*") {
    result = a * b;
  } else if (operator === "/") {
    result = b !== 0 ? a / b : null;
  }

  return result;
}

const output = calculate(3.2, "+", 8);
console.log(output);