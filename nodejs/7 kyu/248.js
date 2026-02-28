// https://www.codewars.com/kata/561046a9f629a8aac000001d/train/javascript

// Passed

function matchArrays(v, r) {
  let numberOfCommonElements = 0;
  for (const item of v) {
    if (r.includes(item)) {
      numberOfCommonElements++;
    }
  }

  return numberOfCommonElements;
}

const output = matchArrays(
  ["incapsulation", "OOP", "array"],
  ["time", "propert", "paralelism", "OOP"],
);
console.log(output);