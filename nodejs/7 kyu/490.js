// https://www.codewars.com/kata/57e2afb6e108c01da000026e/train/javascript

// Passed

function expressionOut(expr) {
  let operatorToPhraseMap = {
    "+": "Plus",
    "-": "Minus",
    "*": "Times",
    "/": "Divided By",
    "**": "To The Power Of",
    "=": "Equals",
    "!=": "Does Not Equal",
  };

  let numToWordMap = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
  };

  let [num1, operator, num2] = expr.split(" ");
  let result = "That's not an operator!";
  if (operator in operatorToPhraseMap) {
    [num1, num2] = [num1, num2].map(Number);
    result = [
      numToWordMap[num1],
      operatorToPhraseMap[operator],
      numToWordMap[num2],
    ].join(" ");
  }
  return result;
}

const output = expressionOut("1 + 3");
console.log(output);