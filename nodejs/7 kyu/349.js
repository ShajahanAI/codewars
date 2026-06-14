// https://www.codewars.com/kata/59557b2a6e595316ab000046/train/javascript

// Passed

function convertHashToArray(hash) {
  let result = Object.keys(hash).map((key) => [key, hash[key]]);
  return result;
}

const output = convertHashToArray({ name: "Jeremy", age: 24 });
console.log(output);