// https://www.codewars.com/kata/57ef016a7b45ef647a00002d/train/javascript

// Passed

function filterHomogenous(arrays) {
  const homogeneousArrays = arrays.filter(
    (subArr) =>
      (subArr.length > 0) &
      subArr.every((elem) => typeof elem === typeof subArr[0])
  );
  return homogeneousArrays;f
}

const output = filterHomogenous([
  [123, 234, 432],
  ["", "abc"],
  [""],
  ["", 1],
  ["", "1"],
  [],
]);
console.log(output);