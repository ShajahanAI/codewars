// https://www.codewars.com/kata/5810085c533d69f4980001cf/train/javascript

// Passed

function calculator(a, b, sign) {
  operationsMap = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => a / b,
  };
  if (
    (typeof a !== "number") |
    (typeof b !== "number") |
    !(sign in operationsMap)
  ) {
    return "unknown value";
  }

  const result = operationsMap[sign](a, b);
  return result;
}

const output = calculator(1, 2, "+");
console.log(output);