// https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/javascript

// Passed

function findAverage(array) {
  let avg;
  if (array.length === 0) {
    avg = 0;
  } else {
    let sum = array.reduce((prev, curr) => prev + curr, 0);
    avg = sum / array.length;
  }

  return avg;
}

const output = findAverage([1, 2, 3, 4]);
console.log(output);