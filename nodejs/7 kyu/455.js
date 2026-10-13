// https://www.codewars.com/kata/63ebadc7879f2500315fa07e/train/javascript

// Passed

function cleanedCounts(data) {
  let result = [...data];
  for (let idx = 0; idx < result.length - 1; idx++) {
    if (result[idx] <= result[idx + 1]) {
      continue;
    }

    result[idx + 1] = result[idx];
  }

  return result;
}

const output = cleanedCounts([1, 1, 2, 2, 1, 2, 2, 2, 2]);
console.log(output);