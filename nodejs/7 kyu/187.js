// https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/javascript

// Passed

function triangular(n) {
  if (n <= 0) {
    return 0;
  }

  let triangularNumber = (n * (n + 1)) / 2;
  return triangularNumber;
}

const output = triangular(4)
console.log(output)