// https://www.codewars.com/kata/5434283682b0fdb0420000e6/train/javascript

// Passed

function caffeineBuzz(n) {
  let result = "mocha_missing!";
  if (n % 12 === 0) {
    result = "Coffee";
  } else if (n % 3 === 0) {
    result = "Java";
  }

  if (n % 2 === 0 && result !== "mocha_missing!") {
    result += "Script";
  }

  return result;
}

const output = caffeineBuzz(9);
console.log(output);