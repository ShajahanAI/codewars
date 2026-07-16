// https://www.codewars.com/kata/55f8ba3be8d585b81e000080/train/javascript

// Passed

function detectOperator(a) {
  let result = "no info";
  let numToOperatorMap = {
    "8039": "Golden Telecom",
    "8050": "MTS",
    "8063": "Life:)",
    "8066": "MTS",
    "8067": "Kyivstar",
    "8068": "Beeline",
    "8093": "Life:)",
    "8095": "MTS",
    "8096": "Kyivstar",
    "8097": "Kyivstar",
    "8098": "Kyivstar",
    "8099": "MTS",
  };

  let numToCheck = String(a).slice(0, 4);
  if (numToCheck in numToOperatorMap) {
    result = numToOperatorMap[numToCheck];
  }

  return result;
}

const output = detectOperator(80931551119);
console.log(output);