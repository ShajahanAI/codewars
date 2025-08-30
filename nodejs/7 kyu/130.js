// https://www.codewars.com/kata/559f89598c0d6c9b31000125/train/javascript

// Passed

function archersReady(archers) {
  return archers.length === 0
    ? false
    : archers.every((archer_arrow_count) => archer_arrow_count >= 5);
}

const output = archersReady([1, 2, 3, 4, 5, 6, 7, 8]);
console.log(output);