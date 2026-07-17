// https://www.codewars.com/kata/5a34b80155519e1a00000009/train/javascript

// Passed

function multipleOfIndex(array) {
  let result = array.filter(
    (num, idx) => (idx === 0 && num === 0) || num % idx === 0,
  );
  return result;
}

const output = multipleOfIndex([22, -6, 32, 82, 9, 25]);
console.log(output);