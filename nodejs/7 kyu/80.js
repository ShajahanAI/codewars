// https://www.codewars.com/kata/53670c5867e9f2222f000225/train/javascript

// Passed

function isOrthogonal(u, v) {
  const products = u.map((num, idx) => num * v[idx]);
  const dotProduct = products.reduce((prev, curr) => prev + curr);
  const isOrthogonal = dotProduct === 0;
  return isOrthogonal;
}

const output = isOrthogonal([1, -2], [2, 1]);
console.log(output);