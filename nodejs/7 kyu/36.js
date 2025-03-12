// https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/javascript

// Passed

function sumOfMinimums(arr) {
  const minArray = arr.map((nestedArr) =>
    nestedArr.reduce((prev, curr) => (prev < curr ? prev : curr))
  );
  return minArray.reduce((prev, curr) => prev + curr);
}

const output = sumOfMinimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100],
]);

console.log(output);