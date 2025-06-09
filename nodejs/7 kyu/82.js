// https://www.codewars.com/kata/5a905c2157c562994900009d/train/javascript

// Passed

function productArray(numbers) {
  const productArray = numbers.map((num, idx) =>
    numbers
      .filter((num, innerIdx) => innerIdx != idx)
      .reduce((prev, curr) => prev * curr, 1)
  );
  return productArray;
}

const output = productArray([10, 3, 5, 6, 2]);
console.log(output);