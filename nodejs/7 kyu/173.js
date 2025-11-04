// https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/train/javascript

// Passed

function maxDiff(list) {
  if (list.length === 0 || list.length === 1) return 0;

  let maximum = Math.max(...list);
  let minimum = Math.min(...list);
  let difference = maximum - minimum;
  return difference;
}

const output = maxDiff([0, 1, 2, 3, 4, 5, 16]);
console.log(output);