// https://www.codewars.com/kata/534ea96ebb17181947000ada/train/javascript

// Passed

function breakChocolate(n, m) {
  if (n <= 0 || m <= 0) {
    return 0;
  }

  let result = n - 1 + n * (m - 1);
  return result;
}

const output = breakChocolate(5, 5);
console.log(output);