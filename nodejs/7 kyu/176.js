// https://www.codewars.com/kata/52705ed65de62b733f000064/train/javascript

// Passed

function sortList(sortBy, list) {
  let sortedArr = list.sort((obj1, obj2) => obj2[sortBy] - obj1[sortBy]);
  return sortedArr;
}

output = sortList("b", [
  { a: 2, b: 2 },
  { a: 3, b: 40 },
  { a: 1, b: 12 },
]);
console.log(output);