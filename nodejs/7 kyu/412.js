// https://www.codewars.com/kata/5c556845d7e0334c74698706/train/javascript

// Passed

function fit_in(a, b, m, n) {
  let squareSideSum = a + b;
  let biggerSide = Math.max(a, b);
  let result =
    (squareSideSum <= m && biggerSide <= n) ||
    (squareSideSum <= n && biggerSide <= m);
  return result;
}

const output = fit_in(1, 2, 3, 2);
console.log(output);