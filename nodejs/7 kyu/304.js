// https://www.codewars.com/kata/69ea4c6708b1c58c36ac735a/train/javascript

// Passed

function wrappingPaper(boxes) {
  let calcTotalSurfaceAreaPlusSlack = (dimensions) => {
    let [l, w, h] = dimensions;
    let areas = [l * w, w * h, l * h];
    let slack = Math.min(...areas);

    let totalSurfaceAreaPlusSlack =
      2 * areas.reduce((a, b) => a + b, 0) + slack;
    return totalSurfaceAreaPlusSlack;
  };

  let result = boxes
    .map((dimensions) => calcTotalSurfaceAreaPlusSlack(dimensions))
    .reduce((a, b) => a + b);
  return result;
}

const output = wrappingPaper([
  [2, 3, 4],
  [1, 1, 1],
]);
console.log(output);