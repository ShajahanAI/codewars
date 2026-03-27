// https://www.codewars.com/kata/5809c661f15835266900010a/train/javascript

// Passed

function doubleEveryOther(a) {
  let result = a.map((val, idx) => (idx % 2 === 1 ? val * 2 : val));
  return result;
}

const output = doubleEveryOther([1, 2, 3, 4]);
console.log(output);