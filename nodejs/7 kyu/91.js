// https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/javascript

// Passed

function findArray(arr1, arr2) {
  const result = arr2
    .map((idx) => (arr1.length > idx ? arr1[idx] : null))
    .filter((elem) => elem !== null);
  return result;
}

const output = findArray([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]);
console.log(output);