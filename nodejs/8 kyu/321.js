// https://www.codewars.com/kata/55a75e2d0803fea18f00009d/train/javascript

// Passed

function slope(points) {
  let [x1, y1, x2, y2] = points;
  let slopeValue = x2 - x1 !== 0 ? String((y2 - y1) / (x2 - x1)) : "undefined";
  return slopeValue;
}

const output = slope([10, 50, 30, 150]);
console.log(output);