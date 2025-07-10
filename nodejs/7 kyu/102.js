// https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/train/javascript

// Passed

function sc(apple) {
  const xCoordinate = apple.findIndex((appleArray) => appleArray.includes("B"));
  const yCoordinate = apple[xCoordinate].indexOf("B");
  const coordinates = [xCoordinate, yCoordinate];
  return coordinates;
}

const output = sc([
  ["A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A"],
  ["A", "B", "A", "A", "A"],
]);
console.log(output);