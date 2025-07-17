// https://www.codewars.com/kata/56044de2aa75e28875000017/train/javascript

// Passed

function compoundArray(a, b) {
  let maxLength = Math.max(a.length, b.length);
  let compoundedArray = [];
  for (let idx = 0; idx < maxLength; idx++) {
    if (idx < a.length) compoundedArray.push(a[idx]);
    if (idx < b.length) compoundedArray.push(b[idx]);
  }

  return compoundedArray;
}

const output = compoundArray([11, 12], [21, 22, 23, 24]);
console.log(output);