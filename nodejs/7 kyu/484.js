// https://www.codewars.com/kata/606b43f4adea6e00425dff42/train/javascript

// Passed

function gridMap(fn, a) {
  let result = [];
  for (let subArrIdx = 0; subArrIdx < a.length; subArrIdx++) {
    let mappedSubArr = a[subArrIdx].map(fn);
    result.push(mappedSubArr);
  }

  return result;
}

const output = gridMap(
  (x) => x + 1,
  [
    [1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [0, 2, 4],
  ],
);
console.log(output);