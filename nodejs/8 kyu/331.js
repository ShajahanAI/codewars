// https://www.codewars.com/kata/57a4d500e298a7952100035d/train/javascript

// Passed

function hexToDec(hexString) {
  let result = parseInt(hexString, 16);
  return result;
}

const output = hexToDec("FF");
console.log(output);